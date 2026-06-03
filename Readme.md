# Health Prediction Application

## Overview

A Flask-based Health Prediction Application that allows users to manage patient records, analyze blood test results, and generate AI-powered health risk assessments using the Google Gemini API.

---

## Features

### Patient Management

* Add Patient Records
* View Patient Records
* Edit Patient Records
* Delete Patient Records

### Data Validation

* Email Validation
* Future Date Restriction for Date of Birth
* Numeric Validation for Blood Test Values

### AI Integration

* Google Gemini API Integration
* Automatic Health Risk Prediction
* AI-Generated Health Remarks

### Database

* SQLite Database
* Persistent Storage of Patient Records

### User Interface

* Bootstrap 5 Responsive Design
* Healthcare-Themed Dashboard
* Edit and Delete Actions with Icons

---

## Application Screenshots

### Home Page

### Add Patient Form


### AI Prediction Result


### Patient Records


### Edit Patient



## Technologies Used

* Python
* Flask
* SQLite
* Bootstrap 5
* Google Gemini API
* HTML
* CSS

---

## CRUD Operations

| Operation | Status |
| --------- | ------ |
| Create    | ✅      |
| Read      | ✅      |
| Update    | ✅      |
| Delete    | ✅      |

---

## AI Prediction Examples

| Input Condition          | AI Remark                      |
| ------------------------ | ------------------------------ |
| Normal Values            | Normal                         |
| High Glucose             | High Diabetes Risk             |
| Low Haemoglobin          | Possible Anaemia               |
| High Cholesterol         | Elevated Cholesterol           |
| Multiple Abnormal Values | Multiple Risk Factors Detected |

---

## Project Structure

HealthPredictionApp/

├── app.py

├── database.py

├── gemini_service.py

├── requirements.txt

├── templates/

│ ├── index.html

│ ├── add_patient.html

│ ├── edit_patient.html

│ └── patients.html

├── database/

│ └── patients.db

└── .env

---

## How To Run

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Create a .env file

GEMINI_API_KEY=YOUR_API_KEY

4. Run the application

python app.py

5. Open browser

http://127.0.0.1:5000

---

## Future Improvements

* User Authentication
* Patient Login Portal
* PDF Health Reports
* Search and Filter Patients
* Dashboard Analytics
