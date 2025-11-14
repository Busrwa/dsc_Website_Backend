from django.contrib import admin
from .models import Blog
from django.http import HttpResponse
from docx import Document
from docx.shared import Pt
from django.core.files.temp import NamedTemporaryFile
import requests


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'image')
    actions = ['export_blogs_word']

    def export_blogs_word(self, request, queryset):
        # Sadece superuser kontrolü
        if not request.user.is_superuser:
            self.message_user(request, "Bu işlemi sadece admin yapabilir!", level='error')
            return None

        document = Document()
        document.add_heading('Blogs Report', 0)

        for blog in queryset.order_by('-published_date'):
            document.add_heading(blog.title, level=1)
            document.add_paragraph(
                f"Published: {blog.published_date.strftime('%Y-%m-%d %H:%M')}"
            )
            document.add_paragraph(blog.content)

            # ------- Cloudinary resim ekleme -------
            if blog.image:
                try:
                    img_url = blog.image.url
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(requests.get(img_url).content)
                    img_temp.flush()
                    document.add_picture(img_temp.name, width=Pt(400))
                except Exception as e:
                    document.add_paragraph(
                        f"Cloudinary görüntüsü eklenemedi: {str(e)}"
                    )
            else:
                document.add_paragraph("Resim yok.")

            document.add_paragraph('\n' + '-' * 50 + '\n')

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename="blogs.docx"'
        document.save(response)
        return response

    export_blogs_word.short_description = "Seçili blogları Word olarak indir"
