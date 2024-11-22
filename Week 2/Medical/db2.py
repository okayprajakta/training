# db.py
import sqlite3
from user1 import Patient

class Database:
    def __init__(self, db_name='medical_db.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._initialize_db()

    def _initialize_db(self):
        """Create the patients table if it doesn't exist."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob TEXT,
            phone_number TEXT,
            email TEXT
        )
        ''')
        self.connection.commit()

    def insert_patient(self, patient_obj):
        """Insert a new patient record."""
        query = '''
        INSERT INTO patients (first_name, last_name, dob, phone_number, email)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (
            patient_obj.first_name,
            patient_obj.last_name,
            patient_obj.dob,
            patient_obj.phone_number,
            patient_obj.email,
        ))
        self.connection.commit()
        return True

    def update_patient(self, patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
        """Update a patient's details."""
        self.cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        patient = self.cursor.fetchone()
        if patient:
            update_query = "UPDATE patients SET"
            values = []
            if first_name:
                update_query += " first_name = ?,"
                values.append(first_name)
            if last_name:
                update_query += " last_name = ?,"
                values.append(last_name)
            if dob:
                update_query += " dob = ?,"
                values.append(dob)
            if phone_number:
                update_query += " phone_number = ?,"
                values.append(phone_number)
            if email:
                update_query += " email = ?,"
                values.append(email)

            update_query = update_query.rstrip(',')  # Remove trailing comma
            update_query += " WHERE patient_id = ?"
            values.append(patient_id)

            self.cursor.execute(update_query, tuple(values))
            self.connection.commit()
            return True
        else:
            return False

    def select_patient_by_id(self, patient_id):
        """Select a patient by ID."""
        self.cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        return self.cursor.fetchone()

    def select_patient_by_phone(self, phone_number):
        """Select patients by phone number."""
        self.cursor.execute("SELECT * FROM patients WHERE phone_number = ?", (phone_number,))
        return self.cursor.fetchall()

    def cleanup(self):
        """Close the cursor and database connection."""
        self.cursor.close()
        self.connection.close()
        return True
