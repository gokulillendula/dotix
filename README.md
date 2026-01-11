JOB SCHEDULER – FULL STACK APPLICATION

A cloud-deployed job scheduling and task execution system built using Django REST Framework and React (Vite). The system allows users to create, prioritize, and manage background jobs that carry dynamic JSON payloads and are executed through a scheduler and webhook-based workflow.

SETUP INSTRUCTIONS

Backend (Django)

Clone the repository
Navigate to backend folder
Create virtual environment
Activate virtual environment
Install dependencies
Apply migrations
Start the server

Commands:

git clone <repository-url>
cd backend
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend runs on:
https://dotix.onrender.com

Frontend (React)

Navigate to frontend folder
Install node dependencies
Start development server

Commands:

cd frontend
npm install
npm run dev

Frontend runs on:
https://dotix-cmg2.vercel.app/

Production Environment

Frontend is deployed on Vercel
Backend API is deployed on Render
Database is PostgreSQL on Render

TECH STACK

Frontend: React.js (Vite)
Backend: Django REST Framework
Authentication: JWT
Database: PostgreSQL
API Communication: Axios
Deployment: Vercel (Frontend), Render (Backend)
Version Control: Git and GitHub

DATABASE SCHEMA (ACTUAL)

Job Table

id
taskName (string)
payload (JSON)
priority (Low, Medium, High)
status (Pending, Running, Failed)
createdAt (timestamp)
updatedAt (timestamp)

Each record in the Job table represents one scheduled task.
The payload column stores dynamic job data in JSON format, allowing flexible execution logic without changing the database schema.

ARCHITECTURE

React Frontend (Vercel)
sends API requests using Axios
to Django REST API (Render)
which interacts with PostgreSQL

Flow:

User creates or deletes a job from the UI
React sends an HTTP request to the backend
Django validates and stores job data
Scheduler reads pending jobs
Webhook or executor processes the job
Status is updated in the database
React UI reflects the updated job state

API DOCUMENTATION

Create Job
POST /api/jobs/

Request body:
{
"taskName": "Send Email",
"payload": {
"to": "user@gmail.com
",
"subject": "Welcome",
"body": "Hello User"
},
"priority": "High"
}

Response:
{
"id": 1,
"taskName": "Send Email",
"payload": {
"to": "user@gmail.com
",
"subject": "Welcome",
"body": "Hello User"
},
"priority": "High",
"status": "Pending",
"createdAt": "2026-01-11T10:32:00Z"
}

Get All Jobs
GET /api/jobs/

Delete Job
DELETE /api/jobs/{id}/

Update Job
PUT /api/jobs/{id}/

WEBHOOK AND JOB EXECUTION FLOW

When a job reaches its scheduled execution time:

The Django scheduler selects the next Pending job
The job is marked as Running
The job payload is sent to a webhook or execution service
The external system performs the required action
On success or failure, the job status is updated

Flow:
Scheduler → Webhook → External Service → Status Update

This design allows the system to integrate with:
Email services
Payment gateways
Automation tools
Notification systems
AI pipelines

AI USAGE LOG

ChatGPT was used as a development assistant for:

System architecture planning
Backend API design and validation
Frontend API integration
Debugging Vite and Axios deployment issues
Deployment configuration on Vercel and Render
Documentation writing

All application code was written, tested, and understood by the developer.
AI was used only to assist development, not to generate the project automatically.

PROJECT OUTCOME

This project demonstrates full-stack system design, RESTful API development, dynamic job execution using JSON payloads, cloud deployment, and a modern React UI. It simulates how real-world task schedulers and automation platforms operate in production systems.