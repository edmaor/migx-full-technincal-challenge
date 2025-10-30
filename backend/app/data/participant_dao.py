from app import settings
from app.domain.participant import Participant
from app.services.mongo_dao import MongoDAO


class ParticipantDAO:
    dao = MongoDAO(settings.DB_URI, settings.DB_NAME, "participants")