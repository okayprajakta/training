'''Import necessary module'''
from Employee_logic import Logic

logic = Logic()

'''Update employee location'''
updated = logic.update_employee_location(1, "Pune")
if updated:
    print("Employee location updated successfully.")
else:
    print("Employee ID not found.")

'''View all employees'''
employees = logic.get_all_employees()
print("All employees:")
for emp in employees:
    print(emp)

'''View employee by ID'''
employee = logic.get_employee_on_empid(1)
if employee:
    print("Employee found:", employee)
else:
    print("Employee not found")

'''View employees by location'''
employees_in_d = logic.get_employee_on_location("Pune")
if employees_in_d:
    print("Employees from the specified location are:")
    for emp in employees_in_d:
        print(emp)
else:
    print("No Employees are from the specified location.")