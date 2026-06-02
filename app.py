from flask import Flask, render_template, request
from database import add_patient

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

        add_patient(
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol
        )

        return "Patient Saved Successfully"

    return render_template("add_patient.html")

if __name__ == "__main__":
    app.run(debug=True)