from django.db import models
from ckeditor.fields import RichTextField


class Settings(models.Model):
    join_link = models.URLField("Hemen Üye Ol Linki", blank=True, null=True)

    def __str__(self):
        return "Site Ayarları"

    class Meta:
        verbose_name = "Ayar"
        verbose_name_plural = "Ayarlar"

from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os

class ArsivEntry(models.Model):
    name = models.CharField(max_length=255)  # Başkan adı
    year = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to='arsiv_images/',  # <-- blog_images yerine arsiv_images
        blank=True, null=True,
        help_text="📷 Görsel oranı 16:9 olmalıdır (örnek: 1600x900, 1920x1080)."
    )
    description = RichTextField()

    def __str__(self):
        return f"{self.name} ({self.year})"

    class Meta:
        verbose_name = "Arşiv Girişi"
        verbose_name_plural = "Arşiv Girişleri"

# Silme ve güncelleme işlemlerinde eski fotoğrafı sil
@receiver(post_delete, sender=ArsivEntry)
def delete_arsiv_photo(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)

@receiver(pre_save, sender=ArsivEntry)
def delete_old_arsiv_photo_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_instance = ArsivEntry.objects.get(pk=instance.pk)
    except ArsivEntry.DoesNotExist:
        return
    old_photo = old_instance.photo
    new_photo = instance.photo
    if old_photo and old_photo != new_photo and os.path.isfile(old_photo.path):
        os.remove(old_photo.path)
