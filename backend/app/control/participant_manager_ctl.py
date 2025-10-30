from typing import Union, Tuple

from app.data.participant_dao import ParticipantDAO
from app.domain.participant import Participant


class ParticipantManagerCTL:
    participant_dao = ParticipantDAO()

    @classmethod
    def create_participant(cls, participant: Participant):
        pass

    @classmethod
    def get_all_participants(cls):
        participants = [Participant(**participant) for participant in cls.participant_dao.dao.read()]
        return participants

    @classmethod
    def get_participant(cls, id: str) -> Tuple[str, Union[Participant, None]]:
        participant = cls.participant_dao.dao.find_by_id(id)
        if participant:
            return "PARTICIPANT", Participant(**participant)
        else:
            return "PARTICIPANT_NOT_FOUND", None

    @classmethod
    def patch_participant(cls, id: str, participant: Participant):
        pass

    @classmethod
    def delete_participant(cls, id: str):
        pass
