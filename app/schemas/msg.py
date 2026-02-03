from pydantic import BaseModel

class Msg(BaseModel):
    msg: str

class Version(BaseModel):
    version: str
    name: str

class SystemInfo(BaseModel):
    status: str
    uptime: str
    load: float
