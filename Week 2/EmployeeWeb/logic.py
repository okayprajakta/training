from Emp import Employee_Update
from db1 import Database


class Logics:
 
    def __init__(self):
        self.db = Database()
  
    def get_Emp(self):
        view = self.db.viewAll()
        return view

    def update_Employee(self, emp_Id, new_Name=None, new_Number=None, new_Location=None):
        return self.db.update_Emp(emp_Id, new_Name, new_Number, new_Location)
    

   
   
    def search_ById(self, emp_Id):
        result = self.db.searchById(emp_Id)
        return result
 
 
    def search_ByLocation(self, emp_Location):
        return self.db.searchByLocation(emp_Location)
           
   
    def closeEmp(self):
        close =  self.db.cleanUp()
        return close