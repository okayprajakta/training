from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from Employee_logic import Logic
'''Import necessaey modules'''

app = FastAPI()
'''Initialize the FastAPI app'''
logic = Logic()
'''Initialize the logic instance'''

class UpdateLocationModel(BaseModel):
    '''A Pydantic model for updating the location of an employee.'''
    location: str

class EmployeeModel(BaseModel):
    '''A Pydantic model for adding a new employee.'''
    empno: int
    empname: str
    location: str
    deptid: int

@app.put("/employees/{empno}", status_code=status.HTTP_200_OK)
def update_employee_location(empno: int, location: UpdateLocationModel):
    '''Endpoint to update the location of an employee using path parameter and request body'''
    if logic.update_employee_location(empno, location.location):
        return {"message": "Employee location updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

@app.get("/employees", status_code=status.HTTP_200_OK)
def get_all_employees():
    '''Endpoint to retrieve all employees.'''
    employees = logic.get_all_employees()
    if employees:
        return {"employees": employees}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")

@app.get("/employees/{empno}", status_code=status.HTTP_200_OK)
def get_employee_by_id(empno: int):
    '''Endpoint to retrieve an employee by employee number as path parameter.'''
    employee = logic.get_employee_on_empid(empno)
    if employee:
        return {"employee": employee}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

@app.get("/employees/location/{location}", status_code=status.HTTP_200_OK)
def get_employees_by_location(location: str):
    '''Endpoint to retrieve employees by location as path parameter.'''
    employees = logic.get_employee_on_location(location)
    if employees:
        return {"employees": employees}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found in this location")

# @app.post("/employees", status_code=status.HTTP_201_CREATED)
# def add_employee(employee: EmployeeModel):
#     '''Endpoint to add a new employee using request body'''
#     new_employee = logic.add_employee(
#         empno=employee.empno,
#         empname=employee.empname,
#         location=employee.location,
#         deptid=employee.deptid
#     )
#     if new_employee:
#         return {"message": "Employee added successfully", "employee": new_employee}
#     else:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add employee")
