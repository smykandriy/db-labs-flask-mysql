from typing import Any, Type

from sqlalchemy import Column, Integer, String

from amusement_park import db
from amusement_park.auth.domain.i_dto import IDto


class Franchise(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "studio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))

    def __repr__(self) -> str:
        return f"Franchise('{self.id}', '{self.name}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "amusement_parks": [amusement_park.name for amusement_park in self.amusement_parks]
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Type["Franchise"]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Franchise(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj