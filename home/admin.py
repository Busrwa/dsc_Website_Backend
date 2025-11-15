from django.contrib import admin
from .models import Settings, ArsivEntry


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("join_link",)


@admin.register(ArsivEntry)
class ArsivEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "photo")  # created_at kaldırıldı
    list_filter = ("year",)
    search_fields = ("name",)
    ordering = ('-created_at',)  # Sıralama burada

    # Detay sayfasında göster ama düzenlenemez
    readonly_fields = ("created_at",)

    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('name', 'year', 'photo', 'description')
        }),
        ('Sistem Bilgileri', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Varsayılan olarak kapalı
        }),
    )