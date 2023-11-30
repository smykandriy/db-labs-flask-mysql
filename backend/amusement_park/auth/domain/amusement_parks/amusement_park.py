from typing import Any, Type

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from amusement_park import db


class AmusementPark(db.Model):
    """
    Model declaration for Amusement Park.
    """

    __tablename__ = "amusement_park"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    max_visitors = Column(Integer, nullable=False)
    location_id = Column(Integer, ForeignKey("location.id"), nullable=False)

    location = relationship("Location", back_populates="amusement_park")
    shows = relationship("Show", back_populates="amusement_park")

    def __repr__(self) -> str:
        return (
            f"AmusementPark('{self.id}', '{self.name}', "
            f"'{self.max_visitors}', '{self.location_id}')"
        )

    def put_into_dto(self, all: bool = None) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as a dictionary
        """
        dto = {
            "id": self.id,
            "name": self.name,
            "max_visitors": self.max_visitors,
            "location_id": self.location_id,
        }
        if all:
            dto["shows"] = [show.put_into_dto() for show in self.shows]
        return dto

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["AmusementPark"]:
        """
        Creates an AmusementPark object from DTO.
        :param dto_dict: DTO object
        :return: AmusementPark object
        """
        obj = AmusementPark(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            max_visitors=dto_dict.get("max_visitors"),
            location_id=dto_dict.get("location_id"),
        )
        return obj
