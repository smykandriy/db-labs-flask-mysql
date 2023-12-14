from sqlalchemy import text

from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain.amusement_parks.amusement_park import AmusementPark


class AmusementParkDAO(GeneralDAO):
    """
    Realisation of Amusement Park data access layer.
    """

    _domain_type = AmusementPark

    def find_by_name(self, name: str) -> list:
        """
        Gets Amusement Park objects from the database table by name.
        :param name: name value
        :return: search objects
        """
        return (
            self._session.query(AmusementPark)
            .filter(AmusementPark.name == name)
            .order_by(AmusementPark.name)
            .all()
        )

    def get_park_with_max_visitors(self):
        return self._session.execute(text("CALL get_park_with_max_visitors()")).all()
