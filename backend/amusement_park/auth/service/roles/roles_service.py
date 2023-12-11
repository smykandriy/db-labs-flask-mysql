from amusement_park.auth.dao import role_dao
from amusement_park.auth.service.general_service import GeneralService


class RoleService(GeneralService):
    """
    Realisation of Role service.
    """

    _dao = role_dao
