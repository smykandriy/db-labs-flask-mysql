from amusement_park.auth.dao import amusement_park_dao, show_dao, attraction_dao
from amusement_park.auth.service.general_service import GeneralService


class AmusementParkService(GeneralService):
    """
    Realisation of Amusement Park service.
    """

    _dao = amusement_park_dao
    _show_dao = show_dao
    _attraction_dao = attraction_dao

    def find_shows_by_amusement_park_id(self, amusement_park_id: int) -> list[object]:
        """
        Gets all shows for a specific Amusement Park.
        :param amusement_park_id: ID of the Amusement Park
        :return: list of Show objects
        """
        return self._show_dao.find_by_amusement_park_id(amusement_park_id)

    def create_show_for_amusement_park(
        self, amusement_park_id: int, show: object
    ) -> object:
        """
        Creates a show for a specific Amusement Park.
        :param amusement_park_id: ID of the Amusement Park
        :param show: Show object to create
        :return: created Show object
        """
        show.amusement_park_id = amusement_park_id
        return self._show_dao.create(show)

    def find_attractions_by_amusement_park_id(
        self, amusement_park_id: int
    ) -> list[object]:
        """
        Gets all attractions for a specific Amusement Park.
        :param amusement_park_id: ID of the Amusement Park
        :return: list of attraction objects
        """
        return self._attraction_dao.find_by_amusement_park_id(amusement_park_id)

    def create_attraction_for_amusement_park(
        self, amusement_park_id: int, attraction: object
    ) -> object:
        """
        Creates a show for a specific Amusement Park.
        :param amusement_park_id: ID of the Amusement Park
        :param attraction: attraction object to create
        :return: created Show object
        """
        attraction.amusement_park_id = amusement_park_id
        return self._attraction_dao.create(attraction)

    def get_park_with_max_visitors(self):
        return self._dao.get_park_with_max_visitors()
