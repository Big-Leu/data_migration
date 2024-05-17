from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'mymodel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    contact_number = Column(String)
    
    name = Column(String)
    
    age = Column(Integer)
    