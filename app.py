from flask import Flask, render_template, request
from flask import redirect, url_for
from database import (
    add_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient,
    delete_patient
)

from gemini_service import generate_health_remark

import re
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]
        glucose = request.form["glucose"]
        haemoglobin = request.form["haemoglobin"]
        cholesterol = request.form["cholesterol"]

        # Email Validation

        if not re.match(
            r"^[^@]+@[^@]+\.[^@]+$",
            email
        ):
            return "Invalid Email Address"

        # Future DOB Validation

        dob_date = datetime.strptime(
            dob,
            "%Y-%m-%d"
        )

        if dob_date > datetime.today():
            return "Date Of Birth Cannot Be In Future"

        # Numeric Validation

        try:

            glucose = float(glucose)
            haemoglobin = float(
                haemoglobin
            )

            cholesterol = float(
                cholesterol
            )

        except ValueError:

            return (
                "Blood Values Must Be Numeric"
            )

        # AI Prediction

        remarks = generate_health_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        # Save Patient

        add_patient(
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        return f"""
<!DOCTYPE html>

<html>

<head>

<title>Prediction Result</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
rel="stylesheet">

</head>

<body class="bg-light">

<div class="container mt-5">

<div class="card shadow">

<div class="card-header bg-success text-white">

<h3>
Patient Saved Successfully
</h3>

</div>

<div class="card-body text-center">

<h4>
🤖 AI Health Assessment
</h4>

<div class="alert alert-info">

<strong>
{remarks}
</strong>

</div>

<a href="/patients"
class="btn btn-primary">

View Patient Records

</a>

<a href="/add"
class="btn btn-success ms-2">

Add Another Patient

</a>

</div>

</div>

</div>

</body>

</html>
"""

    return render_template(
        "add_patient.html"
    )


@app.route("/patients")
def patients():

    all_patients = get_all_patients()

    return render_template(
        "patients.html",
        patients=all_patients
    )


@app.route(
    "/edit/<int:patient_id>",
    methods=["GET", "POST"]
)
def edit_patient(patient_id):

    patient = get_patient_by_id(
        patient_id
    )

    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]
        if not re.match(
            r"^[^@]+@[^@]+\.[^@]+$",email
       ):
            return "Invalid Email Address"
        # Future DOB Validation
        dob_date = datetime.strptime(dob,"%Y-%m-%d")
        if dob_date > datetime.today():
            return "Date Of Birth Cannot Be In Future"
        # Numeric Validation
        try:
            glucose = float(request.form["glucose"])
            haemoglobin = float(
        request.form["haemoglobin"]
    )
            cholesterol = float(request.form["cholesterol"])
            
        except ValueError:
            return ("Blood Values Must Be Numeric")
        # Regenerate AI Remark

        remarks = generate_health_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        update_patient(
            patient_id,
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        return f"""
<!DOCTYPE html>

<html>

<head>

<title>Patient Updated</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
rel="stylesheet">

</head>

<body class="bg-light">

<div class="container mt-5">

<div class="card shadow">

<div class="card-header bg-warning">

<h3>
Patient Updated Successfully
</h3>

</div>

<div class="card-body text-center">

<h4>
🤖 Updated AI Assessment
</h4>

<div class="alert alert-info">

<strong>
{remarks}
</strong>

</div>

<a href="/patients"
class="btn btn-primary">

Back To Patients

</a>

</div>

</div>

</div>

</body>

</html>
"""

    return render_template(
        "edit_patient.html",
        patient=patient
    )

@app.route("/delete/<int:patient_id>")
def delete(patient_id):

    delete_patient(
        patient_id
    )

    return redirect(
        url_for("patients")
    )

if __name__ == "__main__":
    app.run(debug=True)
