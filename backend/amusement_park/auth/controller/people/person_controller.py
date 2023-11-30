from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import person_service


class PersonController(GeneralController):
    """
    Realisation of Person controller.
    """

    _service = person_service
