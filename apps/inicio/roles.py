from rolepermissions.roles import AbstractUserRole


class AdminSistema(AbstractUserRole):
	available_permissions = {
		'create': True,
		'edit': True,
		'delete': True,
	}
class Admin(AbstractUserRole):
	available_permissions = {
		'create': True,
		'edit': True,
		'delete': True,
	}
class JefeArea(AbstractUserRole):
	available_permissions = {
		'create': True,
		'edit': True,
		'delete': True,
	}

class Supervisor(AbstractUserRole):
	available_permissions = {
		'edit': True,
	}

