from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import role_service


class RoleController(GeneralController):
    """
    Realisation of Role controller.
    """

    _service = role_service

    def put_permission_to_role(self, role_id, permission_id):
        self._service.update_role_permission(role_id, permission_id)
