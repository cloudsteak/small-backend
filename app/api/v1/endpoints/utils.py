from typing import Any
from fastapi import APIRouter, Body
from app.core.config import settings
from app.schemas.msg import Msg, Version, SystemInfo
from app.core.security import create_access_token
from app.schemas.token import Token

router = APIRouter()

@router.get("/version", response_model=Version)
def get_version() -> Any:
    """
    Get API version info.
    """
    return {"version": settings.VERSION, "name": settings.PROJECT_NAME}

@router.post("/get-token", response_model=Token)
def get_token(username: str = Body(...)) -> Any:
    """
    Generate a mock JWT token for a given username.
    """
    access_token = create_access_token(subject=username)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/info", response_model=SystemInfo)
def get_system_info() -> Any:
    """
    Get system status information (Mock).
    """
    return {
        "status": "operational",
        "uptime": "12 days, 4 hours",
        "load": 0.42
    }

@router.post("/echo", response_model=Msg)
def echo_message(msg: Msg) -> Any:
    """
    Echo back the provided message.
    """
    return msg

@router.get("/users/me")
def read_user_me() -> Any:
    """
    Get current user (Mock).
    """
    return {"id": 1337, "username": "admin", "full_name": "System Administrator"}
