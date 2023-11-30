from amusement_park.auth.controller.general_controller import GeneralController
from amusement_park.auth.service import show_service, attraction_service


class ShowController(GeneralController):
    """
    Realisation of Show controller.
    """

    _service = show_service


class AttractionController(GeneralController):
    """
    Realisation of Attraction controller.
    """

    _service = attraction_service
