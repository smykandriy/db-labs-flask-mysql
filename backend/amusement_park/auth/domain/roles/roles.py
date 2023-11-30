from typing import Any, Type

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from amusement_park import db


class Role(db.Model):
    """
    Model declaration for Role.
    """

    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)

    person = relationship("Person", back_populates="role")

    def __repr__(self) -> str:
        return f"Role('{self.id}', '{self.name}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {"id": self.id, "name": self.name}

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["Role"]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Role(id=dto_dict.get("id"), name=dto_dict.get("name"))
        return obj
