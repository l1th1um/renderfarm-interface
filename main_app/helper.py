from django.conf import settings

def admin_template():
	return settings.STATIC_URL  + "templates/dashboard/" + settings.ADMIN_TEMPLATE