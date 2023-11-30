from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain import Permission


class PermissionDAO(GeneralDAO):
    """
    Realisation of Role data access layer.
    """

    _domain_type = Permission
