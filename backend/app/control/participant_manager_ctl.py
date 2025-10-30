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
    def get_participant(cls, id: str):
        pass

    @classmethod
    def patch_participant(cls, id: str, participant: Participant):
        pass

    @classmethod
    def delete_participant(cls, id: str):
        pass
