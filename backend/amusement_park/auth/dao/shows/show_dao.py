from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain.shows.show import Show, Attraction


class ShowDAO(GeneralDAO):
    """
    Realisation of Show data access layer.
    """

    _domain_type = Show

    def find_by_amusement_park_id(self, amusement_park_id: int) -> list[object]:
        """
        Gets Show objects from the database table by Amusement Park ID.
        :param amusement_park_id: ID of the Amusement Park
        :return: list of Show objects
        """
        return (
            self._session.query(Show)
            .filter(Show.amusement_park_id == amusement_park_id)
            .order_by(Show.name)
            .all()
        )


class AttractionDAO(GeneralDAO):
    """
    Realisation of Attraction data access layer.
    """

    _domain_type = Attraction

    def find_by_amusement_park_id(self, amusement_park_id: int) -> list[object]:
        """
        Gets Show objects from the database table by Amusement Park ID.
        :param amusement_park_id: ID of the Amusement Park
        :return: list of Show objects
        """
        return (
            self._session.query(Attraction)
            .filter(Attraction.amusement_park_id == amusement_park_id)
            .order_by(Attraction.name)
            .all()
        )
