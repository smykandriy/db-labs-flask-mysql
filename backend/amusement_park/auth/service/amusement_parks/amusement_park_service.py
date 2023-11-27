from amusement_park.auth.dao import amusement_park_dao
from amusement_park.auth.service.general_service import GeneralService


class AmusementParkService(GeneralService):
    """
    Realisation of Amusement Park service.
    """

    _dao = amusement_park_dao
