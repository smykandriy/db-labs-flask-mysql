from amusement_park.auth.dao import role_dao
from amusement_park.auth.service.general_service import GeneralService


class RoleService(GeneralService):
    """
    Realisation of Role service.
    """

    _dao = role_dao

    def update_role_permission(self, role_id, permission_id):
        self._dao.update_role_permission(role_id, permission_id)
