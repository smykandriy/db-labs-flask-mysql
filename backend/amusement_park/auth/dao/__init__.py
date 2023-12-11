from amusement_park.auth.dao.locations.location_dao import LocationDAO
from amusement_park.auth.dao.amusement_parks.amusement_park_dao import AmusementParkDAO
from amusement_park.auth.dao.people.person_dao import PersonDAO
from amusement_park.auth.dao.permissions.permission_dao import PermissionDAO
from amusement_park.auth.dao.roles.roles_dao import RoleDAO
from amusement_park.auth.dao.shows.show_dao import ShowDAO, AttractionDAO
from amusement_park.auth.dao.ticket.ticket_dao import TicketDAO

location_dao = LocationDAO()
amusement_park_dao = AmusementParkDAO()
role_dao = RoleDAO()
person_dao = PersonDAO()
show_dao = ShowDAO()
attraction_dao = AttractionDAO()
permission_dao = PermissionDAO()
ticket_dao = TicketDAO()
