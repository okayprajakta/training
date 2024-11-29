from sqlalchemy.orm import Session
from Emp_model import Employee, User
from datetime import date
from Emp_schema import EmployeeCreate, EmployeeUpdate

# Define date format for employee DOB and DOJ
DATE_FORMAT = "%d/%m/%Y"  # Updated date format (Day/Month/Year)

class EmployeeLogic:
    """
    Employee logic layer for handling operations related to Employee entities.
    Contains CRUD operations for managing employees.
    """
    
    def __init__(self, db: Session):
        """
        Initializes the EmployeeLogic with a database session.

        :param db: Database session to interact with the database.
        """
        self.db = db


    def get_employee_by_id(self, emp_id: int):
        """
        Retrieves an employee by their ID.

        :param emp_id: The unique ID of the employee.
        :return: The employee object or None if not found.
        """
        return self.db.query(Employee).filter(Employee.emp_id == emp_id).first()

    def get_employees_by_name(self, emp_firstname: str = None, emp_lastname: str = None):
        """
        Retrieves employees by their first and/or last name.

        :param emp_firstname: Optional first name of the employee.
        :param emp_lastname: Optional last name of the employee.
        :return: List of employee objects matching the criteria.
        """
        query = self.db.query(Employee)
        
        if emp_firstname:
            query = query.filter(Employee.emp_firstname == emp_firstname)
        if emp_lastname:
            query = query.filter(Employee.emp_lastname == emp_lastname)
        
        return query.all()

    def get_employees_by_grade(self, emp_grade: str):
        """
        Retrieves employees by their grade.

        :param emp_grade: Grade of the employee.
        :return: List of employee objects matching the grade.
        """
        return self.db.query(Employee).filter(Employee.emp_grade == emp_grade).all()

    def get_all_employees(self):
        """
        Retrieves all employees from the database.

        :return: List of all employee objects.
        """
        return self.db.query(Employee).all()

    def update_employee(self, emp_id: int, employee_update: EmployeeUpdate):
        """
        Updates an existing employee's details.

        :param emp_id: The ID of the employee to be updated.
        :param employee_update: EmployeeUpdate Pydantic model containing updated employee data.
        :return: The updated employee object, or None if the employee does not exist.
        """
        # Find employee by ID
        employee = self.db.query(Employee).filter(Employee.emp_id == emp_id).first()
        
        if not employee:
            return None  # Return None if employee not found
        
        # Update fields if provided in the request
        if employee_update.emp_firstname:
            employee.emp_firstname = employee_update.emp_firstname
        if employee_update.emp_lastname:
            employee.emp_lastname = employee_update.emp_lastname
        if employee_update.emp_dob:
            employee.emp_dob = datetime.strptime(employee_update.emp_dob, DATE_FORMAT).date()
        if employee_update.emp_doj:
            employee.emp_doj = datetime.strptime(employee_update.emp_doj, DATE_FORMAT).date()
        if employee_update.emp_grade:
            employee.emp_grade = employee_update.emp_grade

        # Commit the changes to the database
        self.db.commit()
        self.db.refresh(employee)
        
        return employee


class UserLogic:
    """
    User logic layer for handling operations related to User entities.
    Contains CRUD operations for managing users.
    """
    
    def __init__(self, db: Session):
        """
        Initializes the UserLogic with a database session.

        :param db: Database session to interact with the database.
        """
        self.db = db

    def create_user(self, username: str, password: str):
        """
        Creates a new user in the database.

        :param username: Username of the new user.
        :param password: Password for the new user (ideally hashed before saving).
        :return: The newly created user object or None if user already exists.
        """
        # Check if the username already exists
        existing_user = self.db.query(User).filter(User.username == username).first()
        if existing_user:
            return None  # Return None if the username already exists
        
        # Create new user record
        new_user = User(username=username, password=password)
        
        # Add to session and commit to database
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return new_user

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticates a user by checking the username and password.

        :param username: The username of the user.
        :param password: The password of the user.
        :return: True if authentication is successful, False otherwise.
        """
        # Query for the user by username
        user = self.db.query(User).filter(User.username == username).first()
        
        # Check if user exists and password matches
        if user and user.password == password:
            return True  # Return True if authentication is successful
        return False  # Return False if authentication fails
