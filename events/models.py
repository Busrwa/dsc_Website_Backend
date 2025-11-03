from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from ckeditor.fields import RichTextField


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True,
                              help_text="📷 Görsel oranı 16:9 olmalıdır (örnek: 1600x900, 1920x1080).")

    def __str__(self):
        return self.name


# Event silindiğinde image dosyasını da sil
@receiver(post_delete, sender=Event)
def delete_event_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


# Event güncellenirken eski image dosyasını sil (image değişirse)
@receiver(pre_save, sender=Event)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # yeni oluşturuluyorsa bir şey yapma
    try:
        old_instance = Event.objects.get(pk=instance.pk)
    except Event.DoesNotExist:
        return
    old_image = old_instance.image
    new_image = instance.image
    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
