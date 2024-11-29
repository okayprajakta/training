class Employee:
    '''A class to represent the attributes of employee.'''

    def __init__(self,empno,empname,location, deptid):
        '''Initializes an Employee object with the given employee number, name, location, and department ID.'''
        self.empno=empno
        self.empname=empname
        self.location=location
        self.deptid=deptid
    
    def __str__(self):
        '''Returns a string representation of the Employee object.'''
        return f"Employee Number: {self.empno} - Employee Name: {self.empname} - Employee Location: {self.location} - Employee Dept ID: {self.deptid}"