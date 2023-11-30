from typing import Any, Type

from sqlalchemy import Column, Integer, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from amusement_park import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

role_has_permission = Table(
    "role_has_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("permission_id", Integer, ForeignKey("permission.id")),
)

ticket_has_permission = Table(
    "ticket_has_permission",
    Base.metadata,
    Column("ticket_id", Integer, ForeignKey("ticket.id")),
    Column("permission_id", Integer, ForeignKey("permission.id")),
)


class Permission(db.Model):
    """
    Model declaration for Permission.
    """

    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_staff = Column(Boolean, default=False)
    show_id = Column(Integer, ForeignKey("show.id", ondelete="CASCADE"))

    show = relationship("Show", back_populates="permissions")

    def __repr__(self) -> str:
        return f"Permission('{self.id}', '{self.is_staff}', '{self.show_id}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {"id": self.id, "is_staff": self.is_staff, "show_id": self.show_id}

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["Role"]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Permission(
            id=dto_dict.get("id"),
            is_staff=dto_dict.get("is_staff"),
            show_id=dto_dict.get("show_id"),
        )
        return obj
