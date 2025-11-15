#home/admin.py
from django.contrib import admin
from .models import Settings, ArsivEntry


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("join_link",)


@admin.register(ArsivEntry)
class ArsivEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "created_at", "photo")
    list_filter = ("year", "created_at")
    search_fields = ("name",)
    readonly_fields = ("created_at",)  # Sadece okunabilir