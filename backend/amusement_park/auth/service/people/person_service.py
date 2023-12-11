from amusement_park.auth.dao import person_dao
from amusement_park.auth.service.general_service import GeneralService


class PersonService(GeneralService):
    """
    Realisation of Person service.
    """

    _dao = person_dao
