from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(
        upload_to='blog_images/',  # Dosyalar media/blog_images/ içine kaydedilecek
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
