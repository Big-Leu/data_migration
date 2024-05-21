from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from typing import Dict

class ProcessCreateInputSchema(BaseModel):
    process_name: str
    process_data: Dict
    process_attributes: Dict
    owner: str
    
class ProcessDeleteInputSchema(BaseModel):
    uuid: UUID
    
class ProcessCreateOutputSchema(BaseModel):
    uuid: UUID
    process_name: str
    process_data: Dict
    process_attributes: Dict
    owner: str
    created_date: datetime
    updated_date: Optional[datetime]
    deleted_date: Optional[datetime]

    class Config:
        orm_mode = True
