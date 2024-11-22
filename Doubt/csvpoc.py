import csv

class Employee:
    def __init__(self, emp_no, dept_id):
        self.emp_no = emp_no
        self.dept_id = dept_id

    def __repr__(self):
        return f"Employee({self.emp_no}, {self.dept_id})"
    
    def to_csv_row(self):
        return[self.emp_no, self.dept_id]
    
    @classmethod
    def from_csv_row(cls, row):
        emp_no, dept_id=row
        return cls(int(emp_no), int(dept_id))
    
emps=[
    Employee(1, 10),
    Employee(2, 20),
    Employee(3, 30)
    ]

def write_emps_to_csv(emps, filename='emp.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['emp_no', 'dept_id'])

        for employee in emps:
            writer.writerow(employee.to_csv_row())

def read_emps_from_csv(filename='emp.csv'):
    emps = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            employee = Employee.from_csv_row(row)
            emps.append(employee)
    return emps

write_emps_to_csv(emps)
read_emps = read_emps_from_csv()
for emp in read_emps:
    print(emp)
