from fastapi import FastAPI
from logic import Logics
 
app = FastAPI()
logic = Logics()
 
@app.get("/view_all")
def view_Emp():
    view = logic.get_Emp()
    return view
 
@app.put("/update/{empId}")
def update_Emp(emp_Id: int, new_Name: str = None, new_Number: int = None, new_Location: str = None):
    result = logic.update_Employee(emp_Id, new_Name, new_Number, new_Location)
    if isinstance(result, str) and "No employee found" in result:
        return {"error": result}
    return {"success": "Employee updated successfully"}
 
 
@app.get("/search_byid/{empId}")
def search_ById(emp_Id: int):
    employee = logic.search_ById(emp_Id)
    if employee:
        return employee.to_dict()
    return {"error": f"Employee with ID {emp_Id} not found"}
 
 
@app.get("/search_bylocation/{empLocation}")
def search_ByLocation(emp_Location: str):
    employee = logic.search_ByLocation(emp_Location)
    if employee:
        return employee
    return {"error": f"No employees found in location {emp_Location}"}
 
 