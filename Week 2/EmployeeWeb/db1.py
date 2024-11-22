import sqlite3
from Emp import Employee
 
class Database:
 
    def __init__(self):
        self.connection = sqlite3.connect('My_Database.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                number INTEGER NOT NULL,
                location TEXT NOT NULL
                )
            ''')
 
   
    def update_Emp(self, emp_Id, new_Name=None, new_Number=None, new_Location=None):
        self.cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_Id))
        row = self.cursor.fetchone()
 
        if not row:
            return f"No employee found with ID {emp_Id}"
 
        if new_Name:
            self.cursor.execute('UPDATE employees SET name = ? WHERE id = ?', (new_Name, emp_Id))
        if new_Number:
            self.cursor.execute('UPDATE employees SET number = ? WHERE id = ?', (new_Number, emp_Id))
        if new_Location:
            self.cursor.execute('UPDATE employees SET location = ? WHERE id = ?', (new_Location, emp_Id))
 
        self.connection.commit()
        return True
   
 
    def viewAll(self):
        self.cursor.execute('SELECT * FROM employees')
        rows = self.cursor.fetchall()
 
        employees = []
 
        for row in rows:
            emp = Employee(row[0],row[1],row[2],row[3])
            employees.append(emp)
        return employees
   
 
    def searchById(self, empId):
        self.cursor.execute('SELECT * FROM employees WHERE id = ?', (empId,))
        row = self.cursor.fetchone()
        if row:
            return Employee(row[0], row[1], row[2], row[3])
        return None
 
 
    def searchByLocation(self, empLocation):
            self.cursor.execute('SELECT * FROM employees WHERE location = ?', (empLocation,))
            rows = self.cursor.fetchall()  
            employees = []
            for row in rows:
                emp = Employee(row[0],row[1],row[2],row[3])
                employees.append(emp)
            return employees
           
       
 
    def cleanUp(self):
        self.cursor.close()
        self.connection.close()
 
       
 
if __name__ == "__main__":
    Database()