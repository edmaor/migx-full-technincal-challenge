from typing import Union, Tuple

from app.data.participant_dao import ParticipantDAO
from app.domain.participant import Participant


class ParticipantManagerCTL:
    participant_dao = ParticipantDAO()

    @classmethod
    def create_participant(cls, participant: Participant) -> Tuple[str, Union[Participant, None]]:
        """
        Create a new participant.
        :param participant:
        :return:
        """
        participant_id = cls.participant_dao.dao.create(participant.model_dump())
        if participant_id:
            return "PARTICIPANT", Participant(**participant.model_dump())
        else:
            return "PARTICIPANT_NOT_CREATED", None

    @classmethod
    def get_all_participants(cls):
        """
        Get all participants.
        :return:
        """
        participants = [Participant(**participant) for participant in cls.participant_dao.dao.read()]
        return participants

    @classmethod
    def get_participant(cls, id: str) -> Tuple[str, Union[Participant, None]]:
        """
        Get a participant by ID.
        :param id:
        :return:
        """
        participant = cls.participant_dao.dao.find_by_id(id)
        if participant:
            return "PARTICIPANT", Participant(**participant)
        else:
            return "PARTICIPANT_NOT_FOUND", None

    @classmethod
    def patch_participant(cls, id: str, participant: Participant) -> Tuple[str, Union[Participant, None]]:
        """
        Patch a participant specified fields.
        :param id:
        :param participant:
        :return:
        """
        original_participant = cls.participant_dao.dao.find_by_id(id)
        if not original_participant:
            return "PARTICIPANT_NOT_FOUND", None
        else:
            updated_participant = original_participant.copy()
            updated_participant.update(participant.model_dump(exclude_unset=True))
            cls.participant_dao.dao.update({"_id": id}, updated_participant.model_dump())
            return "PARTICIPANT", Participant(**updated_participant)

    @classmethod
    def delete_participant(cls, id: str):
        participant = cls.participant_dao.dao.delete(id)

        if not participant:
            return "PARTICIPANT_NOT_FOUND", None
        else:
            return "PARTICIPANT_DELETED", participant
