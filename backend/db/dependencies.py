from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from backend.db.models.business_process import BusinessProcessModel

engine = create_engine("sqlite:///new.db")
BusinessProcessModel.metadata.create_all(engine)

def get_db_session():
    db = Session(bind=engine)
    return db
