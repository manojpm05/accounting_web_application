from django.contrib import admin
from clients.models import clients
from clients.models import projects

admin.site.register(clients)
admin.site.register(projects)
