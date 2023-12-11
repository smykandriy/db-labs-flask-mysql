from typing import Any, Type

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Table
from sqlalchemy.orm import relationship
from amusement_park import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


person_has_ticket = Table(
    "person_has_ticket",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("person.id")),
    Column("ticket_id", Integer, ForeignKey("ticket.id")),
)


class Person(db.Model):
    """
    Model declaration for Person.
    """

    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone_number = Column(String(13), nullable=True, unique=True)
    email = Column(String(45), nullable=True, unique=True)
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role", back_populates="person")
    # TODO: ticket

    UniqueConstraint("email", name="unique_email")
    UniqueConstraint("phone_number", name="unique_phone_number")

    def __repr__(self) -> str:
        return (
            f"Person('{self.id}', '{self.first_name}', "
            f"'{self.last_name}', '{self.phone_number}', '{self.email}', '{self.role_id}')"
        )

    def put_into_dto(self, all: bool = None) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "role_id": self.role_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["Person"]:
        """
        Creates a Person object from DTO.
        :param dto_dict: DTO object
        :return: Person object
        """
        obj = Person(
            id=dto_dict.get("id"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            phone_number=dto_dict.get("phone_number"),
            email=dto_dict.get("email"),
            role_id=dto_dict.get("role_id"),
        )
        return obj
