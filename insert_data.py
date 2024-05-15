import sqlite3
import json
import re
from sqlalchemy import create_engine, Column, String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from jinja2 import Template

def create_model(class_name, table_name, fields):
    Base = declarative_base()

    class DynamicModel(Base):
        __tablename__ = table_name

        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True, autoincrement=True)
        for field, data_type in fields.items():
            locals()[field] = Column(String)

    DynamicModel.__name__ = class_name

    return DynamicModel



def insert_data(data, Contact):
    try:
        engine = create_engine('sqlite:///new.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        contact = Contact(**data)
        session.add(contact)
        session.commit()
        session.close()
        print("success")
        return "Data inserted successfully!"
    except IntegrityError as e:
        return f"Error: {str(e)}"
    
    
def get_contact():
    conn = sqlite3.connect('new.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM contacts''')
    contacts = cursor.fetchall()
    
    conn.close()
    
    return contacts

def sanitize_input(data):
    print(type(data))
    sanitized_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            sanitized_data[key] = sanitize_input(value)
        elif isinstance(value, list):
            value = ' '.join(str(item) for item in value)
            sanitized_data[key] = re.sub(r'\W+', '', value)
        else:
            sanitized_data[key] = re.sub(r'\W+', '', str(value))
    return sanitized_data

def validate_input(data):
    required_keys = ['name', 'contact_number']
    if not all(key in data for key in required_keys):
        return False
    
    return True

