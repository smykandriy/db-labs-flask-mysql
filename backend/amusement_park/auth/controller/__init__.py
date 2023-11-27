from amusement_park.auth.controller.locations.location_controller import (
    LocationController,
)
from amusement_park.auth.controller.amusement_parks.amusement_park_controller import (
    AmusementParkController,
)
from amusement_park.auth.controller.roles.role_controller import RoleController

location_controller = LocationController()
amusement_park_controller = AmusementParkController()
role_controller = RoleController()
