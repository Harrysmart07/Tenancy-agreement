from pydantic import BaseModel
class user(BaseModel):
    name: str = None
    email: str = None
    password: str = None
    