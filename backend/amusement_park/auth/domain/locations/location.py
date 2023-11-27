from typing import Any, Type

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from amusement_park import db


class Location(db.Model):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(30), nullable=False)
    city = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False, unique=True)

    amusement_park = relationship("AmusementPark", back_populates="location")

    def __repr__(self) -> str:
        return (
            f"Location('{self.id}', '{self.country}', '{self.city}', '{self.address}')"
        )

    def put_into_dto(self, all: bool = None) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "country": self.country,
            "city": self.city,
            "address": self.address,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["Location"]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Location(
            id=dto_dict.get("id"),
            country=dto_dict.get("country"),
            city=dto_dict.get("city"),
            address=dto_dict.get("address"),
        )
        return obj
