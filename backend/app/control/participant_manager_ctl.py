from app.domain.participant import Participant


class ParticipantManagerCtl:
    participant_dao = None

    @classmethod
    def create_participant(cls, participant: Participant):
        pass

    @classmethod
    def get_all_participants(cls):
        pass

    @classmethod
    def get_participant(cls, id: str):
        pass

    @classmethod
    def patch_participant(cls, id: str, participant: Participant):
        pass

    @classmethod
    def delete_participant(cls, id: str):
        pass
