from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.URLField(blank=True, null=True, help_text="📷 Firebase görsel URL'si")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

