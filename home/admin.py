#home/admin.py

from django.contrib import admin
from .models import Settings, ArsivEntry


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("join_link",)


@admin.register(ArsivEntry)
class ArsivEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "photo")
    list_filter = ("year",)
    search_fields = ("name",)