from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain.roles.roles import Role


class RoleDAO(GeneralDAO):
    """
    Realisation of Role data access layer.
    """

    _domain_type = Role
