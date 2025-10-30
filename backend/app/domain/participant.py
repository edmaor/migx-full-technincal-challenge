from pydantic import BaseModel, Field

class Participant(BaseModel):
    class Config:
        populate_by_name = True
    id: str = Field(default=None, alias="_id")
    participant_id: str = None
    subject_id: str = None
    study_group: str = None
    enrollment_date: str = None
    status: str = None
    age: int = None
    gender: str = None