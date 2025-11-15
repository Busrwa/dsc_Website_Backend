from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        folder='blog_images',
        help_text="📷 Görsel en boy oranı 16:9 olmalıdır (örnek: 1600x900, 1920x1080)."
    )
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'