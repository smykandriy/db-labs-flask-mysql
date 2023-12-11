from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain import Person


class PersonDAO(GeneralDAO):
    """
    Realisation of Person data access layer.
    """

    _domain_type = Person

    def find_by_email(self, email: str) -> list[Person]:
        """
        Gets Person objects from the database table by email.
        :param email: email value
        :return: search objects
        """
        return (
            self._session.query(Person)
            .filter(Person.email == email)
            .order_by(Person.email)
            .all()
        )

    def find_by_phone_number(self, phone_number: str) -> list[Person]:
        """
        Gets Person objects from the database table by phone number.
        :param phone_number: phone number value
        :return: search objects
        """
        return (
            self._session.query(Person)
            .filter(Person.phone_number == phone_number)
            .order_by(Person.phone_number)
            .all()
        )
