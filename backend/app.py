from flask import Flask, request, json, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


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
            'timestamp': datetime.utcnow(),
            'repo_name': payload['repository']['full_name']
        }
    elif event_type == 'pull_request':
        action = payload['action']
        pr = payload['pull_request']
        event = {
            'type': 'PULL_REQUEST',
            'author': pr['user']['login'],
            'from_branch': pr['head']['ref'],
            'to_branch': pr['base']['ref'],
            'timestamp': datetime.fromisoformat(pr['updated_at'].rstrip('Z')),
            'repo_name': payload['repository']['full_name'],
            'action': action
        }
        if action == 'closed' and pr['merged']:
            event['type'] = 'MERGE'
        return event
    return None

@app.route("/webhook", methods=['POST'])
def github_webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    if not event_type:
        return jsonify({"error": "Missing X-GitHub-Event header"}), 400

    event = process_webhook(event_type, payload)
    if event:
        db.events.insert_one(event)
        return jsonify({"message": "Event processed successfully"}), 200
    
    return jsonify({"error": "Unhandled event type"}), 400

@app.route("/api/events", methods=['GET'])
def get_events():
    events = list(db.events.find({}, {'_id': 0}).sort('timestamp', -1).limit(10))
    return jsonify(events)

@app.route("/")
def hello_world():
    return "<p>GitHub Webhook Receiver is running!</p>"