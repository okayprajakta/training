# logic.py
from db2 import Database
from user1 import Patient

class Logic:
    def __init__(self):
        self.db = Database()

    def add_patient(self, first_name, last_name, dob, phone_number, email):
        """Add a new patient to the database."""
        patient_obj = Patient(first_name, last_name, dob, phone_number, email)
        return self.db.insert_patient(patient_obj)

    def update_patient(self, patient_id, first_name=None, last_name=None, dob=None, phone_number=None, email=None):
        """Update patient details."""
        return self.db.update_patient(patient_id, first_name, last_name, dob, phone_number, email)

    def get_patient_by_id(self, patient_id):
        """Retrieve a patient by ID."""
        return self.db.select_patient_by_id(patient_id)

    def get_patients_by_phone(self, phone_number):
        """Retrieve patients by phone number."""
        return self.db.select_patient_by_phone(phone_number)

    def cleanup_resources(self):
        """Clean up resources by closing the database."""
        return self.db.cleanup()

# Testing logic functions
if __name__ == '__main__':
    logic = Logic()

    # Adding patients
    print("Adding patients...")
    logic.add_patient('Alice', 'Smith', '1985-06-15', '123-456-7890', 'alice@poc.com')
    logic.add_patient('Bob', 'Johnson', '1992-02-20', '987-654-3210', 'bob@poc.com')

    # Updating a patient
    print("\nUpdating a patient...")
    if logic.update_patient(1, phone_number='111-222-3333', email='alice_new@poc.com'):
        print("Patient updated successfully.")

    # Fetching a patient by ID
    print("\nFetching a patient by ID...")
    patient = logic.get_patient_by_id(1)
    if patient:
        print("Patient Found: ", patient)
    else:
        print("Patient not found.")

    # Fetching patients by phone number
    print("\nFetching patients by phone number...")
    patients = logic.get_patients_by_phone('987-654-3210')
    if patients:
        print("Patients Found: ")
        for p in patients:
            print(p)
    else:
        print("No patients found.")

    # Cleaning up resources
    print("\nCleaning up resources...")
    if logic.cleanup_resources():
        print("Cleanup successful.")
