from Employee_db import Database
'''Import necessary modules'''

class Logic:
    """Handles business logic for employee operations."""

    def __init__(self):
        """Initializes the Logic class with a Database instance."""
        self.db = Database()
    
    def update_employee_location(self, empno, location):
        """Updates the location of an employee."""
        return self.db.update_employee_location(empno, location)

    def get_all_employees(self):
        """Retrieves all employees."""
        return self.db.get_all()

    def get_employee_on_empid(self, empno):
        """Retrieves an employee by employee number."""
        return self.db.get_on_empid(empno)

    def get_employee_on_location(self, location):
        """Retrieves employees by location."""
        return self.db.get_on_location(location)

    # def add_employee(self, empno, empname, location, deptid):
    #     return self.db.add_employee(empno, empname, location, deptid)