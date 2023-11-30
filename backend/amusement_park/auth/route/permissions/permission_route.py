from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request, make_response
from amusement_park.auth.controller import permission_controller
from amusement_park.auth.domain import Permission

permission_bp = Blueprint("permissions", __name__, url_prefix="/permissions/")


@permission_bp.get("")
def get_all_permissions() -> Response:
    """
    Gets all Role objects from the table.
    :return: Response object
    """
    return make_response(
        jsonify(permission_controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@permission_bp.get("/<int:permission_id>")
def get_permission_by_id(permission_id: int) -> Response:
    """
    Gets a Role object by ID.
    :param permission_id: ID of the Role
    :return: Response object
    """
    return make_response(
        jsonify(permission_controller.find_by_id(permission_id)),
        HTTPStatus.OK,
    )


@permission_bp.post("")
def create_permission() -> Response:
    """
    Creates a Role object.
    :return: Response object
    """
    data = request.json
    return make_response(
        jsonify(permission_controller.create(Permission.create_from_dto(data))),
        HTTPStatus.CREATED,
    )


@permission_bp.put("/<int:permission_id>")
def update_permission(permission_id: int) -> Response:
    """
    Updates a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    data = request.json
    permission_controller.update(permission_id, Permission.create_from_dto(data))
    return make_response(
        jsonify(permission_controller.find_by_id(permission_id)), HTTPStatus.OK
    )


@permission_bp.patch("/<int:permission_id>")
def patch_permission(permission_id: int) -> Response:
    """
    Patches a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    data = request.json
    permission_controller.patch(permission_id, data)
    return make_response(
        jsonify(permission_controller.find_by_id(permission_id)), HTTPStatus.OK
    )


@permission_bp.delete("/<int:permission_id>")
def delete_permission(permission_id: int) -> Response:
    """
    Deletes a Role object by ID.
    :param role_id: ID of the Role
    :return: Response object
    """
    permission_controller.delete(permission_id)
    return make_response(
        {"message": f"Permission {permission_id} deleted successfully"}, HTTPStatus.OK
    )
