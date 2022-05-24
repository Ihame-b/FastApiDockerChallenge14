from email.policy import default
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class RegistrationSchemaPublic(BaseModel):
    names: str
    password: str
class Registration(BaseModel):
    names: str
    password: str

class JWTSchema(BaseModel):
    user_id: str
    expire: Optional[datetime]


