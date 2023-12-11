from amusement_park.auth.dao import show_dao, attraction_dao
from amusement_park.auth.service.general_service import GeneralService


class ShowService(GeneralService):
    """
    Realisation of Show service.
    """

    _dao = show_dao


class AttractionService(GeneralService):
    """
    Realisation of Attraction service.
    """

    _dao = attraction_dao
