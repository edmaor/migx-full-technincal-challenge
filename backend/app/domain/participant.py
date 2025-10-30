from pydantic import BaseModel, Field
from typing import Any

class Participant(BaseModel):
    class Config:
        populate_by_name = True
    id: str = Field(default=None, alias="_id")
    name: str
    email: str
    status: str
    data: Any