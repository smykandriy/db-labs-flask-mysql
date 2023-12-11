from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from amusement_park import db
from amusement_park.auth.controller import ticket_controller, permission_controller
from amusement_park.auth.domain import Ticket
from amusement_park.auth.domain.permissions.permission import ticket_has_permission

ticket_bp = Blueprint("tickets", __name__, url_prefix="/tickets/")
session = db.session


@ticket_bp.get("")
def get_all_tickets() -> Response:
    """
    Gets all Ticket objects from the table.
    :return: Response object
    """
    return make_response(
        jsonify(ticket_controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@ticket_bp.get("/<int:ticket_id>")
def get_ticket_by_id(ticket_id: int) -> Response:
    """
    Gets a Ticket object by ID.
    :param ticket_id: ID of the Ticket
    :return: Response object
    """
    return make_response(
        jsonify(ticket_controller.find_by_id(ticket_id)),
        HTTPStatus.OK,
    )


@ticket_bp.get("/<int:ticket_id>/permissions")
def get_role_permissions(ticket_id: int) -> Response:
    """
    Gets a Role object by ID.
    :param ticket_id: ID of the Role
    :return: Response object
    """
    with session.begin():
        permission_ids = (
            session.query(ticket_has_permission.c.permission_id)
            .filter(ticket_has_permission.c.ticket_id == ticket_id)
            .all()
        )

    permissions = [
        permission_controller.find_by_id(permission_id)
        for permission_id in permission_ids
    ]

    return make_response(
        jsonify(permissions),
        HTTPStatus.OK,
    )


@ticket_bp.post("")
def create_ticket() -> Response:
    """
    Creates a Ticket object.
    :return: Response object
    """
    data = request.json
    return make_response(
        jsonify(ticket_controller.create(Ticket.create_from_dto(data))),
        HTTPStatus.CREATED,
    )


@ticket_bp.put("/<int:ticket_id>")
def update_ticket(ticket_id: int) -> Response:
    """
    Updates a Ticket object by ID.
    :param ticket_id: ID of the Ticket
    :return: Response object
    """
    data = request.json
    ticket_controller.update(ticket_id, Ticket.create_from_dto(data))
    return make_response(
        jsonify(ticket_controller.find_by_id(ticket_id)), HTTPStatus.OK
    )


@ticket_bp.patch("/<int:ticket_id>")
def patch_ticket(ticket_id: int) -> Response:
    """
    Patches a Ticket object by ID.
    :param ticket_id: ID of the Ticket
    :return: Response object
    """
    data = request.json
    ticket_controller.patch(ticket_id, data)
    return make_response(
        jsonify(ticket_controller.find_by_id(ticket_id)), HTTPStatus.NO_CONTENT
    )


@ticket_bp.delete("/<int:ticket_id>")
def delete_ticket(ticket_id: int) -> Response:
    """
    Deletes a Ticket object by ID.
    :param ticket_id: ID of the Ticket
    :return: Response object
    """
    ticket_controller.delete(ticket_id)
    return make_response({"message": f"Ticket {ticket_id} deleted"}, HTTPStatus.OK)
