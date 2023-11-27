from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import amusement_park_service


class AmusementParkController(GeneralController):
    """
    Realisation of Amusement Park controller.
    """

    _service = amusement_park_service
