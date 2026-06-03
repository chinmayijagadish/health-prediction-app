from flask import Flask, render_template, request
from database import add_patient
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

        if not re.match(
            r"^[^@]+@[^@]+\.[^@]+$",
            email
        ):
            return "Invalid Email"

        dob_date = datetime.strptime(
            dob,
            "%Y-%m-%d"
        )

        if dob_date > datetime.today():
            return "Future DOB Not Allowed"

        try:

            glucose = float(glucose)
            haemoglobin = float(haemoglobin)
            cholesterol = float(cholesterol)

        except ValueError:

            return "Blood Values Must Be Numeric"

        add_patient(
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol
        )

        return """
        <h2>Patient Saved Successfully</h2>
        <a href='/add'>
        Add Another Patient
        </a>
        """

    return render_template(
        "add_patient.html"
    )


if __name__ == "__main__":
    app.run(debug=True)