#team/models.py
from django.db import models
from cloudinary.models import CloudinaryField


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    photo = CloudinaryField(
        'image',
        blank=True,
        null=True,
        folder='team_photos',
        help_text="Takım üyesi fotoğrafı"
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'