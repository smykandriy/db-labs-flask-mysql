from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from amusement_park.auth.domain.locations.location import Location

from amusement_park.auth.controller import location_controller as controller

location_bp = Blueprint("locations", __name__, url_prefix="/locations/")


@location_bp.get("")
def get_all_locations() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(
        jsonify(controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@location_bp.post("")
def create_location() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    location = Location.create_from_dto(content)
    controller.create(location)
    return make_response(jsonify(location.put_into_dto()), HTTPStatus.CREATED)


@location_bp.get("/<int:location>")
def get_location(location_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    location = controller.find_by_id(location_id)
    return make_response(jsonify(location), HTTPStatus.OK)


@location_bp.put("/<int:location>")
def put_location(location_id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    location = Location.create_from_dto(content)
    controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.delete("/<int:location>")
def delete_client(location_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.OK)
