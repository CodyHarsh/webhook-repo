from flask import Flask, request, json, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

database_url = os.getenv("MONGO_URI")

def connectDatabase():
    client = MongoClient(database_url)
    return client.github_events

db = connectDatabase()

def process_webhook(event_type, payload):
    if event_type == 'push':
        return {
            'type': 'PUSH',
            'author': payload['pusher']['name'],
            'to_branch': payload['ref'].split('/')[-1],
            'timestamp': datetime.utcnow()
        }
    elif event_type == 'pull_request':
        if payload['action'] == 'opened':
            return {
                'type': 'PULL_REQUEST',
                'author': payload['pull_request']['user']['login'],
                'from_branch': payload['pull_request']['head']['ref'],
                'to_branch': payload['pull_request']['base']['ref'],
                'timestamp': datetime.fromisoformat(payload['pull_request']['created_at'].rstrip('Z'))
            }
        elif payload['action'] == 'closed' and payload['pull_request']['merged']:
            return {
                'type': 'MERGE',
                'author': payload['pull_request']['merged_by']['login'],
                'from_branch': payload['pull_request']['head']['ref'],
                'to_branch': payload['pull_request']['base']['ref'],
                'timestamp': datetime.fromisoformat(payload['pull_request']['merged_at'].rstrip('Z'))
            }
    return None

@app.route("/webhook", methods=['POST'])
def githubWebhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.get_json()
    
    print(f"Received event type: {event_type}")
    print(f"Payload: {payload}")

    if not event_type:
        return 'Missing X-GitHub-Event header', 400

    event = process_webhook(event_type, payload)
    if event:
        db.events.insert_one(event)
        print(f"Processed event: {event}")
        return 'Event processed successfully', 200
    
    print(f"Unhandled event type: {event_type}")
    return 'Unhandled event type', 400

@app.route("/api/events", methods=['GET'])
def get_events():
    events = list(db.events.find({}, {'_id': 0}).sort('timestamp', -1).limit(10))
    return jsonify(events)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

