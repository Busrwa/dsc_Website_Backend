#sponsors/models.py
from django.db import models
from cloudinary.models import CloudinaryField


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = CloudinaryField(
        'image',
        blank=True,
        null=True,
        folder='sponsor_logos',
        help_text="Lütfen 600x400 piksel boyutlarında bir logo yükleyin."
    )
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'