from amusement_park.auth.service import location_service
from amusement_park.auth.controller.general_controller import GeneralController


class LocationController(GeneralController):
    """
    Realisation of Location controller.
    """

    _service = location_service
