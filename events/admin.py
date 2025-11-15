#event/admin.py

from django.contrib import admin
from .models import Event
from django.http import HttpResponse
from docx import Document
from docx.shared import Pt
from django.core.files.temp import NamedTemporaryFile
import requests


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'image')
    list_filter = ('date',)
    search_fields = ('name', 'location')
    actions = ['export_events_word']

    def export_events_word(self, request, queryset):
        if not request.user.is_superuser:
            self.message_user(request, "Bu işlemi sadece admin yapabilir!", level='error')
            return None

        document = Document()
        document.add_heading('Events Report', 0)

        for event in queryset.order_by('-date'):
            document.add_heading(event.name, level=1)
            document.add_paragraph(f"Date: {event.date.strftime('%Y-%m-%d %H:%M')}")
            document.add_paragraph(f"Location: {event.location}")
            document.add_paragraph(event.description)

            # Cloudinary resim ekleme
            if event.image:
                try:
                    img_url = event.image.url
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(requests.get(img_url).content)
                    img_temp.flush()
                    document.add_picture(img_temp.name, width=Pt(400))
                except Exception as e:
                    document.add_paragraph(f"Resim eklenemedi: {str(e)}")
            else:
                document.add_paragraph("Resim yok.")

            document.add_paragraph('\n' + '-' * 50 + '\n')

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename="events.docx"'
        document.save(response)
        return response

    export_events_word.short_description = "Seçili eventleri Word olarak indir"