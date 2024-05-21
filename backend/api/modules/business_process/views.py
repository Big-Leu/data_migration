from typing import List
from fastapi import APIRouter, Depends
from backend.schemas.business_process import ProcessCreateInputSchema, ProcessCreateOutputSchema,ProcessDeleteInputSchema
from backend.services.business_process.crud import BusinessProcess
from sqlalchemy.orm import Session
from uuid import UUID
from backend.db.dependencies import get_db_session
from typing import Optional
router = APIRouter()

@router.put("/create", response_model=ProcessCreateOutputSchema)
async def create_process(process_input: ProcessCreateInputSchema, db: Session = Depends(get_db_session)):
    print(type(process_input))
    bp_service = BusinessProcess(db)
    output = await bp_service.create(process_input)
    return output
@router.post("/update/{uuid}", response_model=ProcessCreateOutputSchema)
async def Update_process(uuid: UUID, process_input: ProcessCreateInputSchema, db: Session = Depends(get_db_session)):
    print(type(process_input))
    bp_service = BusinessProcess(db)
    output = await bp_service.Update(process_input, uuid)
    return output
@router.get("/list", response_model=List[ProcessCreateOutputSchema])
async def list_processes(db: Session = Depends(get_db_session)):
    bp = BusinessProcess(db)
    output = await bp.LIST()
    return output
@router.delete("/delete/{uuid}", response_model=Optional[ProcessCreateOutputSchema])
async def delete_process(uuid: UUID, db: Session = Depends(get_db_session)):
    bp = BusinessProcess(db)
    process_input = ProcessDeleteInputSchema(uuid=uuid)
    deleted_instance = await bp.Delete(process_input)
    return deleted_instance
@router.get("/read/{uuid}", response_model=Optional[ProcessCreateOutputSchema])
async def read_process(uuid: UUID, db: Session = Depends(get_db_session)):
    bp = BusinessProcess(db)
    process_input = ProcessDeleteInputSchema(uuid=uuid)
    instance = await bp.Read(process_input)
    return instance