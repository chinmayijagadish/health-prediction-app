import sqlite3

def create_database():

    conn = sqlite3.connect("database/patients.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dob TEXT NOT NULL,
        email TEXT NOT NULL,
        glucose REAL NOT NULL,
        haemoglobin REAL NOT NULL,
        cholesterol REAL NOT NULL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_patient(
        name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol):

    conn = sqlite3.connect("database/patients.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (
        name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol
    )
    VALUES
    (?, ?, ?, ?, ?, ?)
    """,
    (
        name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol
    ))

    conn.commit()
    conn.close()

def get_all_patients():

    conn = sqlite3.connect(
        "database/patients.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM patients"
    )

    patients = cursor.fetchall()

    conn.close()

    return patients

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")