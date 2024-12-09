from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Emp_model import Base

DATABASE_URL = 'sqlite:///Employees.db' 

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()