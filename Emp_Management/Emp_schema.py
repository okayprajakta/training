from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeCreate(BaseModel):
    """
    Pydantic model for creating a new employee.
    Contains all necessary fields for employee creation.
    """
    emp_id: int  # Employee ID (Primary Key)
    emp_firstname: str  # Employee's First Name
    emp_lastname: str  # Employee's Last Name
    emp_dob: Optional[date]  # Date of Birth, Optional field
    emp_doj: Optional[date]  # Date of Joining, Optional field
    emp_grade: Optional[str]  # Employee's Grade, Optional field

    class Config:
        """Config class to include attributes from the model."""
        from_attributes = True  # Ensures that attributes can be accessed using 'from_attributes'

class EmployeeUpdate(BaseModel):
    """
    Pydantic model for updating an existing employee.
    Only the fields that are provided will be updated.
    """
    emp_firstname: Optional[str]  # Employee's First Name (Optional for updates)
    emp_lastname: Optional[str]  # Employee's Last Name (Optional for updates)
    emp_dob: Optional[date]  # Date of Birth (Optional for updates)
    emp_doj: Optional[date]  # Date of Joining (Optional for updates)
    emp_grade: Optional[str]  # Employee's Grade (Optional for updates)

    class Config:
        """Config class to include attributes from the model."""
        from_attributes = True  # Ensures that attributes can be accessed using 'from_attributes'

class UserCreate(BaseModel):
    """
    Pydantic model for creating a new user.
    Contains required fields for user creation.
    """
    username: str  # Username (unique identifier for the user)
    password: str  # Password for the user (should be hashed in real applications)

    class Config:
        """Config class to include attributes from the model."""
        from_attributes = True  # Ensures that attributes can be accessed using 'from_attributes'
