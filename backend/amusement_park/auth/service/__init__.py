from amusement_park.auth.service.locations.location_service import LocationService
from amusement_park.auth.service.amusement_parks.amusement_park_service import (
    AmusementParkService,
)
from amusement_park.auth.service.roles.roles_service import RoleService

location_service = LocationService()
amusement_park_service = AmusementParkService()
role_service = RoleService()
