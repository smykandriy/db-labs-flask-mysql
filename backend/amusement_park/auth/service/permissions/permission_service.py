from amusement_park.auth.dao import permission_dao
from amusement_park.auth.service.general_service import GeneralService


class PermissionService(GeneralService):
    """
    Realisation of Role data access layer.
    """

    _dao = permission_dao
