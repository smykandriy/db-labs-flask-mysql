from amusement_park.auth.controller.locations.location_controller import (
    LocationController,
)
from amusement_park.auth.controller.amusement_parks.amusement_park_controller import (
    AmusementParkController,
)
from amusement_park.auth.controller.people.person_controller import (
    PersonController,
)
from amusement_park.auth.controller.permissions.permission_controller import (
    PermissionController,
)
from amusement_park.auth.controller.roles.role_controller import RoleController
from amusement_park.auth.controller.shows.show_controller import (
    ShowController,
    AttractionController,
)
from amusement_park.auth.controller.ticket.ticket_controller import TicketController

location_controller = LocationController()
amusement_park_controller = AmusementParkController()
role_controller = RoleController()
person_controller = PersonController()
show_controller = ShowController()
attraction_controller = AttractionController()
permission_controller = PermissionController()
ticket_controller = TicketController()
