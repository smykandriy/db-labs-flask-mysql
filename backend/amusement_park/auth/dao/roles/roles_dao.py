from sqlalchemy import text

from amusement_park import db
from amusement_park.auth.dao.general_dao import GeneralDAO
from amusement_park.auth.domain.roles.roles import Role


class RoleDAO(GeneralDAO):
    """
    Realisation of Role data access layer.
    """

    _domain_type = Role
    _session = db.session

    def create(self, obj: object) -> object:
        """
        Creates object in database table.
        :param obj: object to create in Database
        :return: created object
        """
        self._session.execute(text(f"CALL insert_role('{obj.name}')"))
        self._session.commit()
        return obj

    def update_role_permission(self, role_id, permission_id):
        self._session.execute(text(f"CALL insert_role_permission({role_id}, {permission_id})"))
        self._session.commit()
