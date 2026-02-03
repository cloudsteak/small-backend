from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "small-backend"
    API_V1_STR: str = "/v1"
    SECRET_KEY: str = "super-secret-key-for-development-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # Additional endpoints mock data
    SYSTEM_NAME: str = "T-1000"
    VERSION: str = "0.1.0"

    model_config = {"case_sensitive": True}


settings = Settings()
