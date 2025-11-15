#home/models.py

from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Settings(models.Model):
    join_link = models.URLField("Hemen Üye Ol Linki", blank=True, null=True)

    def __str__(self):
        return "Site Ayarları"

    class Meta:
        verbose_name = "Ayar"
        verbose_name_plural = "Ayarlar"


class ArsivEntry(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=50)
    photo = CloudinaryField(
        'image',
        blank=True,
        null=True,
        folder='arsiv_images',
        help_text="📷 Görsel oranı 16:9 olmalıdır (örnek: 1600x900, 1920x1080)."
    )
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)  # Eklenme tarihi

    def __str__(self):
        return f"{self.name} ({self.year})"

    class Meta:
        ordering = ['-created_at']  # En son eklenen en üstte
        verbose_name = "Arşiv Girişi"
        verbose_name_plural = "Arşiv Girişleri"