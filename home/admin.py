from django.contrib import admin
from .models import Settings

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("join_link",)

from .models import Settings, ArsivEntry

@admin.register(ArsivEntry)
class ArsivEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "year")
