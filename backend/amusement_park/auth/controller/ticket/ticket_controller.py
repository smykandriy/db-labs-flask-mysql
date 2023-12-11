from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import ticket_service


class TicketController(GeneralController):
    """
    Realization of Ticket controller.
    """

    _service = ticket_service
