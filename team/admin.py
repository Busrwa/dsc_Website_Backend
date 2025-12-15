#team/admin.py
from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'photo')
    search_fields = ('name', 'role')
    list_filter = ('role',)