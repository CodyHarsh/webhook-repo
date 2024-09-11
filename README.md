# Project Name

This repository contains both the frontend and backend components of our application.

## Project Repositories

- Webhook Github Repository: [github.com/CodyHarsh/webhook-repo](https://github.com/CodyHarsh/webhook-repo)
- Action Repo Github Repository: [github.com/CodyHarsh/action-repo](https://github.com/CodyHarsh/action-repo)

## Live Links

- Backend Live Link: [techstax-eyjv.onrender.com](https://techstax-eyjv.onrender.com)
- Frontend Live Link: [webhook-repo-phi.vercel.app](https://webhook-repo-phi.vercel.app)

## Project Structure

```
project-root/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md (this file)
```

## Frontend

The frontend is built with [Your Frontend Framework/Library, e.g., React, Vue, Angular].

### Setup and Running

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

The frontend will be available at `http://localhost:5173`.


## Backend

The backend is built with Flask and uses MongoDB for data storage.

### Setup and Running

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set the MongoDB URI environment variable:
   ```
   export MONGO_URI='your_mongodb_uri_here'
   ```

5. Run the Flask application:
   ```
   flask --app app run
   ```

The backend will be available at `http://localhost:5000`.

## Environment Variables

- `MONGO_URI`: The connection string for your MongoDB database.
