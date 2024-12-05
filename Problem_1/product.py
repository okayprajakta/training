from sqlalchemy import Column,Integer, String,Float
from db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, nullable=False,index=True)
    price=Column(Float,nullable=False,index=True)

    def __repr__(self):
        return f"id :{self.id} name :{self.name} price: {self.price}"