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

## 📸 Application Screenshots

### 🏠 Home Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/331c91b0-827e-488c-8f6c-d4fcb0997ccd" width="800">
</p>

---

### ➕ Add Patient Form

<p align="center">
  <img src="https://github.com/user-attachments/assets/bfbed449-3a94-42e3-a872-10df40e4027b" width="800">
</p>

---

### 🤖 AI Prediction Result

<p align="center">
  <img src="https://github.com/user-attachments/assets/923d4c95-4478-43d1-8f05-99431eaecf47" width="800">
</p>

---

### 📋 Patient Records

<p align="center">
  <img src="https://github.com/user-attachments/assets/70802f4e-b4f9-4a8e-903c-e734148e2e00" width="800">
</p>

---

### ✏️ Edit Patient

<p align="center">
  <img src="https://github.com/user-attachments/assets/f47164d5-38bc-407f-9b9b-ba6e0859cbe6" width="800">
</p>


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
