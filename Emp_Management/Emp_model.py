from sqlalchemy import Integer, Column, String, Date
from sqlalchemy.orm import declarative_base

# Create the base class for declarative models
Base = declarative_base()

class Employee(Base):
    """
    Employee model to represent employees in the database.
    
    Attributes:
        emp_id (int): Primary key for the employee.
        emp_firstname (str): First name of the employee.
        emp_lastname (str): Last name of the employee.
        emp_dob (date): Date of birth of the employee.
        emp_doj (date): Date of joining of the employee.
        emp_grade (str): Grade of the employee.
    """
    __tablename__ = 'employees'  # Define the table name

    # Define the columns for the Employee table
    emp_id = Column(Integer, primary_key=True, index=True)  # Primary key
    emp_firstname = Column(String, nullable=False)  # First name (cannot be null)
    emp_lastname = Column(String, nullable=False)  # Last name (cannot be null)
    emp_dob = Column(Date, nullable=True)  # Date of birth (can be null)
    emp_doj = Column(Date, nullable=True)  # Date of joining (can be null)
    emp_grade = Column(String, nullable=True)  # Employee grade (can be null)


class User(Base):
    """
    User model to represent users for authentication in the database.
    
    Attributes:
        id (int): Primary key for the user.
        username (str): Unique username for login.
        password (str): Password for the user.
    """
    __tablename__ = 'users'  # Define the table name

    # Define the columns for the User table
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    username = Column(String, unique=True, index=True, nullable=False)  # Unique username (cannot be null)
    password = Column(String, nullable=False)  # Password (cannot be null)
