from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Emp_db import get_db
from Emp_logic import EmployeeLogic, UserLogic
from Emp_schema import  EmployeeUpdate, UserCreate
from typing import Optional

# Create FastAPI app instance
app = FastAPI()

@app.post("/register/", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Registers a new user in the system.

    :param user: The UserCreate Pydantic model containing the user data.
    :param db: The database session dependency.
    :return: A message with the created username.
    :raises HTTPException: If the username already exists.
    """
    user_logic = UserLogic(db)
    created_user = user_logic.create_user(user.username, user.password)
    
    # If the username already exists, return an error message
    if not created_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    return {"username": created_user.username}

@app.post("/login/", status_code=status.HTTP_200_OK)
def login(username: str, password: str, db: Session = Depends(get_db)):
    """
    Authenticates a user based on their username and password.

    :param username: The username of the user.
    :param password: The password of the user.
    :param db: The database session dependency.
    :return: A message indicating login success.
    :raises HTTPException: If credentials are invalid.
    """
    user_logic = UserLogic(db)
    
    # Check if authentication is successful
    if not user_logic.authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful"}


@app.get("/employee/{emp_id}", status_code=status.HTTP_200_OK)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    """
    Retrieves an employee by their unique employee ID.

    :param emp_id: The ID of the employee.
    :param db: The database session dependency.
    :return: The employee object if found.
    :raises HTTPException: If the employee is not found.
    """
    employee_logic = EmployeeLogic(db)
    employee = employee_logic.get_employee_by_id(emp_id)
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee

@app.get("/employee/grade/{emp_grade}", status_code=status.HTTP_200_OK)
def get_employees_by_grade(emp_grade: str, db: Session = Depends(get_db)):
    """
    Retrieves all employees by their grade.

    :param emp_grade: The grade of the employee.
    :param db: The database session dependency.
    :return: List of employees with the given grade.
    """
    employee_logic = EmployeeLogic(db)
    return employee_logic.get_employees_by_grade(emp_grade)

@app.put("/employee/{emp_id}", status_code=status.HTTP_200_OK)
def update_employee(emp_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    """
    Updates an existing employee's information.

    :param emp_id: The ID of the employee to be updated.
    :param employee: The EmployeeUpdate Pydantic model with updated employee data.
    :param db: The database session dependency.
    :return: A success message upon successful update.
    :raises HTTPException: If the employee does not exist or cannot be updated.
    """
    employee_logic = EmployeeLogic(db)
    updated_employee = employee_logic.update_employee(emp_id, employee)
    
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found or not updated")
    
    return {"message": "Employee updated successfully"}
