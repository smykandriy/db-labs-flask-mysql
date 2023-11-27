from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import role_service


class RoleController(GeneralController):
    """
    Realisation of Role controller.
    """

    _service = role_service
