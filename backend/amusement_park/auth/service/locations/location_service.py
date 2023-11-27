from amusement_park.auth.dao import location_dao
from amusement_park.auth.service.general_service import GeneralService


class LocationService(GeneralService):
    """
    Realisation of Country service.
    """

    _dao = location_dao
