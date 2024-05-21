"""
For all modules, add the routers in this file.

"""
from fastapi.routing import APIRouter

from backend.api.modules import business_process

api_router = APIRouter()
api_router.include_router(business_process.router, prefix="/process", tags=["process"])
