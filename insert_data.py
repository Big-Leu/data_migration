import sqlite3
import json
import re
from sqlalchemy import create_engine, Column, String,Integer,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from alembic import command
from alembic.config import Config
from generated_model import MyModel

def insert_data(data):
    try:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        print(MyModel.__table__.columns.keys())
        engine = create_engine('sqlite:///new.db')
        Session = sessionmaker(bind=engine)
        inspector = inspect(engine)
        print(inspector.get_table_names())
        if 'mymodel' not in inspector.get_table_names():
            MyModel.__table__.create(bind=engine)
        session = Session()
        contact = MyModel(**data)
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
    
    cursor.execute('''SELECT * FROM mymodel''')
    contacts = cursor.fetchall()
    
    conn.close()
    
    return contacts

def sanitize_input(data):
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

