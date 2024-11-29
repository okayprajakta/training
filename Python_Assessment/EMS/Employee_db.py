'''Importing necessary modules'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''Define the Database URL'''
DATABASE_URL = "sqlite:///./employee.db"

'''Create the SQLAlchemy engine'''
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

'''Create the Base class for the models'''
Base = declarative_base()

'''Define the Employee model (table)'''
class Employee(Base):
    __tablename__ = 'employees'

    empno = Column(Integer, primary_key=True, index=True)
    empname = Column(String, nullable=False)
    location = Column(String, nullable=False)
    deptid = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Employee(empno={self.empno}, empname={self.empname}, location={self.location}, deptid={self.deptid})"

'''Create the session maker'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''Create the tables in the database'''
Base.metadata.create_all(bind=engine)

'''CRUD Operations'''
class Database:
    def __init__(self):
        '''Initializes the Database class with a session maker'''
        self.Session = SessionLocal

    def create_table(self):
        '''Creates the tables in the database'''
        Base.metadata.create_all(bind=engine)

    def update_employee_location(self, empno, location):
        '''Updates the location of an employee'''
        session = self.Session()
        employee = session.query(Employee).filter(Employee.empno == empno).first()
        if employee:
            employee.location = location
            session.commit()
            session.close()
            return True
        session.close()
        return False

    def get_all(self):
        '''Retrieves all employees'''
        session = self.Session()
        employees = session.query(Employee).all()
        session.close()
        return employees

    def get_on_empid(self, empno):
        '''Retrieves an employee by employee number'''
        session = self.Session()
        employee = session.query(Employee).filter(Employee.empno == empno).first()
        session.close()
        return employee

    def get_on_location(self, location):
        '''Retrieves employees by location'''
        session = self.Session()
        employees = session.query(Employee).filter(Employee.location == location).all()
        session.close()
        return employees
    
    # def add_employee(self, empno, empname, location, deptid):
    #     '''Adds a new employee to the database'''
    #     session = self.Session()
    #     new_employee = Employee(empno=empno, empname=empname, location=location, deptid=deptid)
    #     session.add(new_employee)
    #     session.commit()
    #     session.close()
    #     return new_employee