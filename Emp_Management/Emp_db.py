from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Emp_model import Base  # Import the Base class from the model file

# Define the database URL (SQLite database for simplicity)
DATABASE_URL = 'sqlite:///Employee_assessment.db'

# Create the engine that connects to the SQLite database
# The "check_same_thread" argument ensures that SQLite allows the connection from multiple threads
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session local class for database interactions
# The session will manage the database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables based on the models defined in the Base
Base.metadata.create_all(bind=engine)

def get_db():
    """
    Dependency function that provides a session to the database.
    
    This function will be used in FastAPI or other frameworks to get a 
    database session for each request. It ensures that the session is closed 
    once the request is processed.
    """
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to the caller
    finally:
        db.close()  # Ensure the session is closed after the operation
