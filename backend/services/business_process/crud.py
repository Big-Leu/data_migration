from backend.db.models.business_process import BusinessProcessModel
from backend.db.dependencies import get_db_session
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import update,delete
from sqlalchemy.orm import class_mapper
from backend.schemas.business_process import ProcessCreateInputSchema,ProcessDeleteInputSchema
from fastapi import FastAPI,Request,HTTPException
import uuid
from typing import Optional

class BusinessProcess():
    def __init__(self, session: Session) -> None:
        self.session = get_db_session()
    def serialize(model_instance):
        columns = [c.key for c in class_mapper(model_instance.__class__).columns]
        return {c: getattr(model_instance, c) for c in columns}
    
    async def create(self, process_input: ProcessCreateInputSchema):
        data = process_input.dict()
        data['uuid'] = uuid.uuid4()  # Generate a new UUID
        bp = BusinessProcessModel(**data)
        self.session.add(bp)
        self.session.commit()
        self.session.refresh(bp)
        return {**bp.__dict__}
    
    async def Update(self, process_input: ProcessCreateInputSchema, uuid1):
        data = process_input.dict()

        # Query the instance before updating
        instance_to_update = self.session.query(BusinessProcessModel).filter_by(uuid=uuid1).first()

        if instance_to_update is None:
            return None

        stmt = (
            update(BusinessProcessModel).
            where(BusinessProcessModel.uuid == uuid1).
            values(**data)
        )
        self.session.execute(stmt)
        self.session.commit()

        # Query the updated instance
        updated_instance = self.session.query(BusinessProcessModel).filter_by(uuid=uuid1).first()

        # Return the updated instance as a dictionary
        return {**updated_instance.__dict__}
    
    async def Delete(self, process_input: ProcessCreateInputSchema) -> Optional[BusinessProcessModel]:
        data = process_input.dict()

        # Query the instance before deletion
        instance_to_delete = self.session.query(BusinessProcessModel).filter_by(uuid=data['uuid']).first()

        if instance_to_delete is None:
            return None

        stmt = (
            delete(BusinessProcessModel).
            where(BusinessProcessModel.uuid == data['uuid'])
        )
        self.session.execute(stmt)
        self.session.commit()

        return instance_to_delete
    async def LIST(self):
        result = self.session.query(BusinessProcessModel).all()
        if not result:
            raise HTTPException(status_code=404, detail="No items found")
        data = []
        for item in result:
            item_dict = {key: value for key, value in item.__dict__.items() if not key.startswith('_')}
            data.append(item_dict)
        return data

    async def Read(self, process_input: ProcessDeleteInputSchema):
        data = process_input.dict()
        instance = self.session.query(BusinessProcessModel).filter_by(uuid=data['uuid']).first()
        return instance
    def close(self):
        self.session.close()

# businessProcess = BusinessProcess()

# def get_business_process_instance():
#     if businessProcess is None:
#         businessProcess = BusinessProcess()
#     return businessProcess