from datetime import date
from typing import Any, Type

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from amusement_park import db


class Ticket(db.Model):
    """
    Model declaration for Ticket.
    """

    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self) -> str:
        return f"Ticket('{self.id}', '{self.name}', '{self.date}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["Ticket"]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Ticket(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            date=date.fromisoformat(dto_dict.get("date")),
        )
        return obj
