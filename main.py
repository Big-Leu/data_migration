from typing import List, Dict
from insert_data import validate_input,sanitize_input
from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from generated_model import MyModel
from sqlalchemy.orm import Session
from sqlalchemy import insert,update,delete
from sqlalchemy.orm import class_mapper
from sqlalchemy.exc import SQLAlchemyError


import json
def serialize(model_instance):
    """Transforms a model instance into a dictionary."""
    columns = [c.key for c in class_mapper(model_instance.__class__).columns]
    return {c: getattr(model_instance, c) for c in columns}
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
engine = create_engine("sqlite:///new.db")
session = Session(bind=engine)

@app.post("/api/v1/form/contact")
async def read_root(request: Request):
        data =await request.json()
        if not data:
            return JSONResponse({"message": "INVALID"}, status_code=400)

        
        sanitized_data = sanitize_input(data)
        
        if not validate_input(sanitized_data):
            print("returned from validate_input")
            return JSONResponse({"message": "INVALID"}, status_code=400)
        
        try:
            session.execute(insert(MyModel), data)
            session.commit()
            return JSONResponse({"message": "Ok"}, status_code=200)
        except SQLAlchemyError as e:
            session.rollback()
            return JSONResponse({"message": "An error occurred: " + str(e)}, status_code=400)
        finally:
            session.close()
@app.post("/api/v1/form/delete")
async def delete_item(request: Request):
    data = await request.json()
    try:
        stmt = (
            delete(MyModel).
            where(MyModel.id == data['id'])
        )
        session.execute(stmt)
        session.commit()
        return JSONResponse({"message": "Ok"}, status_code=200)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="An error occurred: " + str(e))
    finally:
        session.close()

@app.post("/api/v1/form/update")
async def update_item(request: Request):
    data = await request.json()
    try:
        stmt = (
            update(MyModel).
            where(MyModel.id == data['id']).
            values(**data)
        )
        session.execute(stmt)
        session.commit()
        return JSONResponse({"message": "Ok"}, status_code=200)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="An error occurred: " + str(e))
    finally:
        session.close()

@app.get("/api/v1/form/detail", response_model=List[Dict])
async def read_item():
    result = session.query(MyModel).all()
    if not result:
        raise HTTPException(status_code=404, detail="No items found")
    data = [serialize(item) for item in result]
    return data
