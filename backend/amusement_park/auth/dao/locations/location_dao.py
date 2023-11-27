from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain.locations.location import Location


class LocationDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """

    _domain_type = Location

    def find_by_address(self, address: str) -> list:
        """
        Gets Country objects from database table by name.
        :param address: address value
        :return: search objects
        """
        return (
            self._session.query(Location)
            .filter(Location.address == address)
            .order_by(Location.address)
            .all()
        )
