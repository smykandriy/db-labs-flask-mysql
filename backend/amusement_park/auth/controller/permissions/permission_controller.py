from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import permission_service


class PermissionController(GeneralController):
    """
    Realisation of Permission controller.
    """

    _service = permission_service
