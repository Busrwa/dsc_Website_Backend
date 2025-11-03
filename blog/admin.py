from django.contrib import admin
from .models import Blog
from django.http import HttpResponse
from docx import Document
from docx.shared import Pt
import os


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
            document.add_paragraph(f"Published: {blog.published_date.strftime('%Y-%m-%d %H:%M')}")
            document.add_paragraph(blog.content)

            if blog.image:
                img_path = blog.image.path
                if os.path.exists(img_path):
                    try:
                        document.add_picture(img_path, width=Pt(400))
                    except Exception as e:
                        document.add_paragraph(f"Image yüklenemedi: {str(e)}")
                else:
                    document.add_paragraph("Resim dosyası bulunamadı.")

            document.add_paragraph('\n' + '-' * 50 + '\n')

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename="blogs.docx"'
        document.save(response)
        return response

    export_blogs_word.short_description = "Seçili blogları Word olarak indir"
