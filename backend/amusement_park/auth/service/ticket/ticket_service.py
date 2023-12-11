from amusement_park.auth.dao import ticket_dao
from amusement_park.auth.service.general_service import GeneralService


class TicketService(GeneralService):
    """
    Realization of Ticket service.
    """

    _dao = ticket_dao
