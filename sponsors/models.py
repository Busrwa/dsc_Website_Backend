from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='sponsor_logos/', blank=True, null=True,
                             help_text="Lütfen 600x400 piksel boyutlarında bir logo yükleyin.")
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# Sponsor silindiğinde logo dosyasını da sil
@receiver(post_delete, sender=Sponsor)
def delete_sponsor_logo(sender, instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)


# Sponsor güncellenirken eski logo dosyasını sil (logo değişirse)
@receiver(pre_save, sender=Sponsor)
def delete_old_logo_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # yeni oluşturuluyorsa bir şey yapma
    try:
        old_instance = Sponsor.objects.get(pk=instance.pk)
    except Sponsor.DoesNotExist:
        return
    old_logo = old_instance.logo
    new_logo = instance.logo
    if old_logo and old_logo != new_logo:
        if os.path.isfile(old_logo.path):
            os.remove(old_logo.path)
