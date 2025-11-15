#event/models.py
from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        folder='event_images',
        help_text="📷 Görsel oranı 16:9 olmalıdır (örnek: 1600x900, 1920x1080)."
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'