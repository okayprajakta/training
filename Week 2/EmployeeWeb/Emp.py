class Employee:
 
    def __init__(self, emp_Id, emp_Name, emp_Number, emp_Location):
        self.emp_Id = emp_Id
        self.emp_Name = emp_Name
        self.emp_Number = emp_Number
        self.emp_Location = emp_Location

 
    def __repr__(self):
        return f"Employee({self.emp_Id}, {self.emp_Name}, {self.emp_Number}, {self.emp_Location})"
 
    def to_dict(self):
        return {
            "empId": self.emp_Id,
            "empName": self.emp_Name,
            "empNumber": self.emp_Number,
            "empLocation": self.emp_Location
        }

class Employee_Update:
    def __init__(self, emp_Id, new_Name=None, new_Number=None, new_Location=None):
        self.emp_Id = emp_Id
        self.new_Name = new_Name
        self.new_Number = new_Number
        self.new_Location = new_Location

    def __repr__(self):
        return f"EmployeeUpdate({self.emp_Id}, {self.new_Name}, {self.new_Number}, {self.new_Location})"
    