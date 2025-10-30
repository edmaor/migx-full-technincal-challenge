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
        participant_data = participant.model_dump()
        participant_data.pop("id", None)
        participant_id = cls.participant_dao.dao.create(participant_data)
        if participant_id:
            participant.id = participant_id
            return "PARTICIPANT", participant
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
            updated_participant.pop("_id", None)
            if cls.participant_dao.dao.update_one(id, updated_participant):
                updated_participant = Participant(**updated_participant)
                updated_participant.id = id
                return "PARTICIPANT", updated_participant
            else:
                return "PARTICIPANT_NOT_UPDATED", None

    @classmethod
    def delete_participant(cls, id: str):
        participant = cls.participant_dao.dao.delete(id)

        if not participant:
            return "PARTICIPANT_NOT_FOUND", None
        else:
            return "PARTICIPANT_DELETED", participant
