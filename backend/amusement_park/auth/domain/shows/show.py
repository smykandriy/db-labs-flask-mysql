from typing import Any, Type

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from amusement_park import db


class Show(db.Model):
    """
    Model declaration for Show.
    """

    __tablename__ = "show"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    description = Column(String(45), nullable=True)
    date = Column(String(45), nullable=True)
    amusement_park_id = Column(Integer, ForeignKey("amusement_park.id"), nullable=False)

    amusement_park = relationship("AmusementPark", back_populates="shows")
    attraction = relationship("Attraction", back_populates="show")
    permissions = relationship(
        "Permission", back_populates="show", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"Show('{self.id}', '{self.name}', "
            f"'{self.description}', '{self.date}', '{self.amusement_park_id}')"
        )

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "amusement_park_id": self.amusement_park_id,
        }

    @staticmethod
    def create_from_dto(
        dto_dict: dict[str, Any], amusement_park_id: int = None
    ) -> Type["Show"]:
        """
        Creates a Show object from DTO.
        :param dto_dict: DTO object
        :return: Show object
        """
        if amusement_park_id is None:
            return Show(
                id=dto_dict.get("id"),
                name=dto_dict.get("name"),
                description=dto_dict.get("description"),
                date=dto_dict.get("date"),
                amusement_park_id=dto_dict.get("amusement_park_id"),
            )
        obj = Show(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            date=dto_dict.get("date"),
            amusement_park_id=amusement_park_id,
        )
        return obj


class Attraction(Show):
    """
    Model declaration for Attraction, inherited from Show.
    """

    __tablename__ = "attraction"

    has_queue = Column(Boolean, nullable=False)
    has_reservation = Column(Boolean, nullable=False)
    show_id = Column(Integer, ForeignKey("show.id"), primary_key=True)

    show = relationship("Show", back_populates="attraction")

    def __repr__(self) -> str:
        return (
            f"Attraction('{self.id}', '{self.name}', "
            f"'{self.description}', '{self.date}', '{self.amusement_park_id}', "
            f"'{self.has_queue}', '{self.has_reservation}')"
        )

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship.
        :return: DTO object as a dictionary
        """
        dto = super().put_into_dto()
        dto.update(
            {
                "has_queue": self.has_queue,
                "has_reservation": self.has_reservation,
            }
        )
        return dto

    @staticmethod
    def create_from_dto(
        dto_dict: dict[str, Any], amusement_park_id: int = None
    ) -> Type["Attraction"]:
        """
        Creates an Attraction object from DTO.
        :param dto_dict: DTO object
        :return: Attraction object
        """
        if amusement_park_id is None:
            return Attraction(
                id=dto_dict.get("id"),
                name=dto_dict.get("name"),
                description=dto_dict.get("description"),
                date=dto_dict.get("date"),
                amusement_park_id=dto_dict.get("amusement_park_id"),
                has_queue=dto_dict.get("has_queue"),
                has_reservation=dto_dict.get("has_reservation"),
            )
        obj = Attraction(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            date=dto_dict.get("date"),
            amusement_park_id=amusement_park_id,
            has_queue=dto_dict.get("has_queue"),
            has_reservation=dto_dict.get("has_reservation"),
        )
        return obj
