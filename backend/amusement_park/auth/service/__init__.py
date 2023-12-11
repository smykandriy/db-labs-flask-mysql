from amusement_park.auth.service.locations.location_service import LocationService
from amusement_park.auth.service.amusement_parks.amusement_park_service import (
    AmusementParkService,
)
from amusement_park.auth.service.people.person_service import PersonService
from amusement_park.auth.service.permissions.permission_service import PermissionService
from amusement_park.auth.service.roles.roles_service import RoleService
from amusement_park.auth.service.shows.show_service import (
    ShowService,
    AttractionService,
)
from amusement_park.auth.service.ticket.ticket_service import TicketService

location_service = LocationService()
amusement_park_service = AmusementParkService()
role_service = RoleService()
person_service = PersonService()
show_service = ShowService()
attraction_service = AttractionService()
permission_service = PermissionService()
ticket_service = TicketService()
