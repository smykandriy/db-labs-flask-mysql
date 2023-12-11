from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain import Ticket


class TicketDAO(GeneralDAO):
    """
    Realization of Ticket data access layer.
    """

    _domain_type = Ticket
