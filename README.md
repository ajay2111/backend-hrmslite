HRMS Lite – Full-Stack Coding Assignment
Overview

HRMS Lite is a lightweight Human Resource Management System designed to manage employee records and track daily attendance. This web-based application simulates essential HR operations with a simple, usable, and professional interface.

The project evaluates end-to-end full-stack development skills, including frontend development, backend API design, database modeling, validations, and deployment readiness.

Features
1. Employee Management

Add a new employee with:

Employee ID (unique)

Full Name

Email Address

Department

View a list of all employees

Delete an employee

2. Attendance Management

Mark attendance for an employee with:

Date

Status (Present / Absent)

View attendance records for each employee

Tech Stack
Layer	Technology / Framework
Frontend	React.js / JavaScript
Backend	Python / Django or FastAPI
Database	MongoDB / PostgreSQL / MySQL
Deployment	Vercel / Netlify (Frontend)
	Render / Railway (Backend)

Note: You may replace the above stack with your preferred technologies.

Installation & Local Setup

Clone the repository

git clone <repository-url>
cd hrms-lite


Backend Setup

cd backend
# Create virtual environment (Python)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver   # Django
# or
uvicorn main:app --reload     # FastAPI


Frontend Setup

cd frontend
# Install dependencies
npm install

# Run development server
npm start


Access the Application

Frontend: http://localhost:3000

Backend API: http://localhost:8000 (or as configured)

Assumptions & Limitations

Single admin user (no authentication implemented)

Advanced HR features (leave management, payroll) are out of scope

Basic validation implemented for required fields and email format

Duplicate employee entries are prevented

Focus is on functional usability over excessive features

Deployment

The application has been deployed and is publicly accessible:

Frontend URL: https://hrms-lite-frontend.vercel.app

Backend API URL: https://hrms-lite-backend.onrender.com

Ensure both frontend and backend are connected properly.

Bonus Features (Optional)

Filter attendance records by date

Display total present days per employee

Basic dashboard summary with counts or tables

These are implemented only if the core functionality is complete.

Project Structure
hrms-lite/
├── frontend/          # React application
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/           # Django / FastAPI backend
│   ├── app/ / hrms/
│   ├── requirements.txt
│   └── main.py / manage.py
└── README.md

API Endpoints (Sample)
Employee

GET /employees – List all employees

POST /employees – Add new employee

DELETE /employees/:id – Delete employee

Attendance

GET /attendance/:employeeId – Get attendance records

POST /attendance – Mark attendance

All endpoints return meaningful HTTP status codes and error messages for invalid requests.

Author

Your Name – Full-Stack Developer

License

This project is for educational purposes only.

If you want, I can also make a visually appealing version with badges, screenshots, and live demo links ready for GitHub that will look pro
