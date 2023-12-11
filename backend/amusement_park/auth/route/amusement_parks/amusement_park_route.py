from http import HTTPStatus
from os import abort

from flask import Blueprint, Response, jsonify, request, make_response

from amusement_park.auth.controller import (
    amusement_park_controller,
    show_controller,
    attraction_controller,
)
from amusement_park.auth.domain import AmusementPark
from amusement_park.auth.domain.shows.show import Show, Attraction

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


@amusement_park_bp.get("/<int:amusement_park_id>/shows")
def get_all_shows(amusement_park_id: int) -> Response:
    """
    Gets all shows for a specific Amusement Park.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    amusement_park = amusement_park_controller.find_by_id(amusement_park_id)
    if amusement_park is None:
        abort(HTTPStatus.NOT_FOUND)
    shows = amusement_park_controller._service.find_shows_by_amusement_park_id(
        amusement_park_id
    )

    shows_as_dicts = [show.put_into_dto() for show in shows]

    return make_response(
        jsonify(shows_as_dicts),
        HTTPStatus.OK,
    )


@amusement_park_bp.post("/<int:amusement_park_id>/shows")
def create_show(amusement_park_id: int) -> Response:
    """
    Creates a show for a specific Amusement Park.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    data = request.json
    show = Show.create_from_dto(data, amusement_park_id=amusement_park_id)
    created_show = show_controller.create(show)

    return make_response(
        jsonify(created_show),
        HTTPStatus.CREATED,
    )


@amusement_park_bp.get("/<int:amusement_park_id>/shows/<int:show_id>")
def get_show_by_id(amusement_park_id: int, show_id: int) -> Response:
    """
    Gets an show object by ID.
    :param show_id: ID of the show
    :return: Response object
    """
    return make_response(
        jsonify(show_controller.find_by_id(show_id)),
        HTTPStatus.OK,
    )


@amusement_park_bp.put("/<int:amusement_park_id>/shows/<int:show_id>")
def update_show(amusement_park_id: int, show_id: int) -> Response:
    """
    Updates a show object by ID.
    :param show_id: ID of the show
    :return: Response object
    """
    data = request.json
    show_controller.update(show_id, Show.create_from_dto(data))
    return make_response(jsonify(show_controller.find_by_id(show_id)), HTTPStatus.OK)


@amusement_park_bp.patch("/<int:amusement_park_id>/shows/<int:show_id>")
def patch_show(amusement_park_id: int, show_id: int) -> Response:
    """
    Patches an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    data = request.json
    show_controller.patch(show_id, data)
    return make_response(jsonify(show_controller.find_by_id(show_id)), HTTPStatus.OK)


@amusement_park_bp.delete("/<int:amusement_park_id>/shows/<int:show_id>")
def delete_show(amusement_park_id: int, show_id: int) -> Response:
    """
    Deletes an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    show_controller.delete(show_id)
    return make_response(
        {"message": f"Show {show_id} deleted successfully"}, HTTPStatus.OK
    )


@amusement_park_bp.get("/<int:amusement_park_id>/attractions")
def get_all_attractions(amusement_park_id: int) -> Response:
    """
    Gets all shows for a specific Amusement Park.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    amusement_park = amusement_park_controller.find_by_id(amusement_park_id)
    if amusement_park is None:
        abort(HTTPStatus.NOT_FOUND)
    attractions = (
        amusement_park_controller._service.find_attractions_by_amusement_park_id(
            amusement_park_id
        )
    )

    attractions_as_dicts = [attraction.put_into_dto() for attraction in attractions]

    return make_response(
        jsonify(attractions_as_dicts),
        HTTPStatus.OK,
    )


@amusement_park_bp.post("/<int:amusement_park_id>/attractions")
def create_attraction(amusement_park_id: int) -> Response:
    """
    Creates a show for a specific Amusement Park.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    data = request.json
    attraction = Attraction.create_from_dto(data, amusement_park_id=amusement_park_id)
    created_show = attraction_controller.create(attraction)

    return make_response(
        jsonify(created_show),
        HTTPStatus.CREATED,
    )


@amusement_park_bp.get("/<int:amusement_park_id>/attractions/<int:attraction_id>")
def get_attraction_by_id(amusement_park_id: int, attraction_id: int) -> Response:
    """
    Gets an attraction object by ID.
    :param attraction_id: ID of the attraction
    :return: Response object
    """
    return make_response(
        jsonify(attraction_controller.find_by_id(attraction_id)),
        HTTPStatus.OK,
    )


@amusement_park_bp.put("/<int:amusement_park_id>/attractions/<int:attraction_id>")
def update_attraction(amusement_park_id: int, attraction_id: int) -> Response:
    """
    Updates a show object by ID.
    :param show_id: ID of the show
    :return: Response object
    """
    data = request.json
    attraction_controller.update(attraction_id, Attraction.create_from_dto(data))
    return make_response(
        jsonify(attraction_controller.find_by_id(attraction_id)), HTTPStatus.OK
    )


@amusement_park_bp.patch("/<int:amusement_park_id>/attractions/<int:attraction_id>")
def patch_attraction(amusement_park_id: int, attraction_id: int) -> Response:
    """
    Patches an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    data = request.json
    attraction_controller.patch(attraction_id, data)
    return make_response(
        jsonify(attraction_controller.find_by_id(attraction_id)), HTTPStatus.OK
    )


@amusement_park_bp.delete("/<int:amusement_park_id>/attractions/<int:attraction_id>")
def delete_attraction(amusement_park_id: int, attraction_id: int) -> Response:
    """
    Deletes an Amusement Park object by ID.
    :param amusement_park_id: ID of the Amusement Park
    :return: Response object
    """
    attraction_controller.delete(attraction_id)
    return make_response(
        {"message": f"Attraction {attraction_id} deleted successfully"}, HTTPStatus.OK
    )
