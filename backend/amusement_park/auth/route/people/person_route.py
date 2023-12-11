from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from amusement_park import db
from amusement_park.auth.controller import person_controller, ticket_controller
from amusement_park.auth.domain import Person
from amusement_park.auth.domain.people.person import person_has_ticket

person_bp = Blueprint("people", __name__, url_prefix="/people/")
session = db.session


@person_bp.get("")
def get_all_people() -> Response:
    """
    Gets all Person objects from the table.
    :return: Response object
    """
    return make_response(
        jsonify(person_controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@person_bp.get("/<int:person_id>")
def get_person_by_id(person_id: int) -> Response:
    """
    Gets a Person object by ID.
    :param person_id: ID of the Person
    :return: Response object
    """
    return make_response(
        jsonify(person_controller.find_by_id(person_id)),
        HTTPStatus.OK,
    )


@person_bp.get("/<int:person_id>/tickets")
def get_person_tickets(person_id: int) -> Response:
    """
    Gets a Role object by ID.
    :param ticket_id: ID of the Role
    :return: Response object
    """
    with session.begin():
        ticket_ids = (
            session.query(person_has_ticket.c.ticket_id)
            .filter(person_has_ticket.c.person_id == person_id)
            .all()
        )

    tickets = [ticket_controller.find_by_id(ticket_id) for ticket_id in ticket_ids]

    return make_response(
        jsonify(tickets),
        HTTPStatus.OK,
    )


@person_bp.post("")
def create_person() -> Response:
    """
    Creates a Person object.
    :return: Response object
    """
    data = request.json
    return make_response(
        jsonify(person_controller.create(Person.create_from_dto(data))),
        HTTPStatus.CREATED,
    )


@person_bp.put("/<int:person_id>")
def update_person(person_id: int) -> Response:
    """
    Updates a Person object by ID.
    :param person_id: ID of the Person
    :return: Response object
    """
    data = request.json
    person_controller.update(person_id, Person.create_from_dto(data))
    return make_response("", HTTPStatus.NO_CONTENT)


@person_bp.patch("/<int:person_id>")
def patch_person(person_id: int) -> Response:
    """
    Patches a Person object by ID.
    :param person_id: ID of the Person
    :return: Response object
    """
    data = request.json
    person_controller.patch(person_id, data)
    return make_response("", HTTPStatus.NO_CONTENT)


@person_bp.delete("/<int:person_id>")
def delete_person(person_id: int) -> Response:
    """
    Deletes a Person object by ID.
    :param person_id: ID of the Person
    :return: Response object
    """
    person_controller.delete(person_id)
    return make_response("", HTTPStatus.NO_CONTENT)


@person_bp.delete("")
def delete_all_people() -> Response:
    """
    Deletes all Person objects.
    :return: Response object
    """
    person_controller.delete_all()
    return make_response("", HTTPStatus.NO_CONTENT)
