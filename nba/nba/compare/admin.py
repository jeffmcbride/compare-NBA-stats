# cities/admin.py
from django.contrib import admin

from .models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "name")

admin.site.register(Team, TeamAdmin)