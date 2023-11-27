from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response

from amusement_park.auth.controller import amusement_park_controller
from amusement_park.auth.domain import AmusementPark

amusement_park_bp = Blueprint(
    "amusement_parks", __name__, url_prefix="/amusement-parks/"
)


@amusement_park_bp.get("")
def get_all_amusement_parks() -> Response:
    """
    Gets all Amusement Park objects from the table.
    :return: Response object
    """
    return make_response(
        jsonify(amusement_park_controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@amusement_park_bp.get("/<int:amusement_park_id>")
def get_amusement_park_by_id(amusement_park_id: int) -> Response:
    """
    Gets an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    return make_response(
        jsonify(amusement_park_controller.find_by_id(amusement_park_id)),
        HTTPStatus.OK,
    )


@amusement_park_bp.post("")
def create_amusement_park() -> Response:
    """
    Creates an Amusement Park object.
    :return: Response object
    """
    data = request.json
    return make_response(
        jsonify(amusement_park_controller.create(AmusementPark.create_from_dto(data))),
        HTTPStatus.CREATED,
    )


@amusement_park_bp.put("/<int:amusement_park_id>")
def update_amusement_park(amusement_park_id: int) -> Response:
    """
    Updates an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    data = request.json
    amusement_park_controller.update(
        amusement_park_id, AmusementPark.create_from_dto(data)
    )
    return make_response("", HTTPStatus.NO_CONTENT)


@amusement_park_bp.patch("/<int:amusement_park_id>")
def patch_amusement_park(amusement_park_id: int) -> Response:
    """
    Patches an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    data = request.json
    amusement_park_controller.patch(amusement_park_id, data)
    return make_response("", HTTPStatus.NO_CONTENT)


@amusement_park_bp.delete("/<int:amusement_park_id>")
def delete_amusement_park(amusement_park_id: int) -> Response:
    """
    Deletes an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    amusement_park_controller.delete(amusement_park_id)
    return make_response("", HTTPStatus.NO_CONTENT)


@amusement_park_bp.delete("")
def delete_all_amusement_parks() -> Response:
    """
    Deletes all Amusement Park objects.
    :return: Response object
    """
    amusement_park_controller.delete_all()
    return make_response("", HTTPStatus.NO_CONTENT)
