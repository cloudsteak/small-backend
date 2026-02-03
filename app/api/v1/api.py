from fastapi import APIRouter
from app.api.v1.endpoints import items, utils

api_router = APIRouter()
api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
