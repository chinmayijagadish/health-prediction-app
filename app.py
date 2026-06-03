from flask import Flask, render_template, request
from database import add_patient, get_all_patients
from gemini_service import generate_health_remark
import re
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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
            return "Date of Birth Cannot Be In Future"

        # Numeric Validation

        try:

            glucose = float(glucose)
            haemoglobin = float(haemoglobin)
            cholesterol = float(cholesterol)

        except ValueError:

            return "Blood Values Must Be Numeric"

        # Gemini AI Prediction

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

<div class="row justify-content-center">

<div class="col-md-8">

<div class="card shadow border-0">

<div class="card-header bg-success text-white">

<h3 class="mb-0">
Patient Saved Successfully
</h3>

</div>

<div class="card-body text-center">

<h4 class="mb-4">
🤖 AI Health Assessment
</h4>

<div class="alert alert-info">

<strong>
{remarks}
</strong>

</div>

<div class="mt-4">

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


if __name__ == "__main__":
    app.run(debug=True)