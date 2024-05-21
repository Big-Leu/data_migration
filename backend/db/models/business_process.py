from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from backend.db.base import Base

class BusinessProcessModel(Base):
    __tablename__ = "business_processes"

    uuid = Column(UUID(as_uuid=True), primary_key=True, index=True)
    process_name = Column(String, index=True)
    process_data = Column(JSON)
    process_attributes = Column(JSON)
    owner = Column(String)
    created_date = Column(DateTime, default=datetime.now)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_date = Column(DateTime)

    # owner = relationship("User", back_populates="processes")

