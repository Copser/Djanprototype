from django.contrib import admin

from .models import Event


# Registering Event model into admin
admin.site.register(Event)
