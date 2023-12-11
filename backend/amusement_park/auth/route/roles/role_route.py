from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response

from amusement_park import db
from amusement_park.auth.controller import role_controller, permission_controller
from amusement_park.auth.domain import Role
from amusement_park.auth.domain.permissions.permission import role_has_permission

role_bp = Blueprint("roles", __name__, url_prefix="/roles/")
session = db.session


@role_bp.get("")
def get_all_roles() -> Response:
    """
    Gets all Role objects from the table.
    :return: Response object
    """
    return make_response(
        jsonify(role_controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@role_bp.get("/<int:role_id>")
def get_role_by_id(role_id: int) -> Response:
    """
    Gets a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    return make_response(
        jsonify(role_controller.find_by_id(role_id)),
        HTTPStatus.OK,
    )


@role_bp.get("/<int:role_id>/permissions")
def get_role_permissions(role_id: int) -> Response:
    """
    Gets a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    with session.begin():
        permission_ids = (
            session.query(role_has_permission.c.permission_id)
            .filter(role_has_permission.c.role_id == role_id)
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


@role_bp.post("")
def create_role() -> Response:
    """
    Creates a Role object.
    :return: Response object
    """
    data = request.json
    return make_response(
        jsonify(role_controller.create(Role.create_from_dto(data))),
        HTTPStatus.CREATED,
    )


@role_bp.put("/<int:role_id>")
def update_role(role_id: int) -> Response:
    """
    Updates a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    data = request.json
    role_controller.update(role_id, Role.create_from_dto(data))
    return make_response("", HTTPStatus.NO_CONTENT)


@role_bp.patch("/<int:role_id>")
def patch_role(role_id: int) -> Response:
    """
    Patches a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    data = request.json
    role_controller.patch(role_id, data)
    return make_response("", HTTPStatus.NO_CONTENT)


@role_bp.delete("/<int:role_id>")
def delete_role(role_id: int) -> Response:
    """
    Deletes a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    role_controller.delete(role_id)
    return make_response("", HTTPStatus.NO_CONTENT)


@role_bp.delete("")
def delete_all_roles() -> Response:
    """
    Deletes all Role objects.
    :return: Response object
    """
    role_controller.delete_all()
    return make_response("", HTTPStatus.NO_CONTENT)
