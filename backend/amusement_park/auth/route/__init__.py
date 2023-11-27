from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .locations.location_route import location_bp
    from .amusement_parks.amusement_park_route import amusement_park_bp
    from .roles.role_route import role_bp

    app.register_blueprint(location_bp)
    app.register_blueprint(amusement_park_bp)
    app.register_blueprint(role_bp)
