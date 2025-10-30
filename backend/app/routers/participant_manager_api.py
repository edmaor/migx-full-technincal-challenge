from fastapi import APIRouter
from typing import List

from starlette import status

from app.domain.participant import Participant
from app.control.participant_manager_ctl import ParticipantManagerCTL
router = APIRouter(tags=["Participant Manager"], prefix="/migx/participant")


@router.post("", response_model=Participant, response_model_by_alias=False, status_code=status.HTTP_201_CREATED)
async def create_participant(participant: Participant):
    return {"message": "Hello World"}

@router.get("", response_model=List[Participant], response_model_by_alias=False)
async def get_all_participants():
    participants = ParticipantManagerCTL.get_all_participants()
    return participants

@router.get("/{id}")
async def get_participant(id: str):
    return {"message": f"Hello {id}"}

@router.patch("/{id}")
async def patch_participant(id: str, participant: Participant):
    return {"message": f"Hello {id}"}

@router.delete("/{id}")
async def delete_participant(id: str):
    return {"message": f"Hello {id}"}