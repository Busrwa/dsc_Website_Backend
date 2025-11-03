from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(
        blank=True,
        null=True
    )  # Cloudinary kendi dosya yolunu yönetiyor
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
