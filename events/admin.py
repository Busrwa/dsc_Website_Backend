from django.contrib import admin
from .models import Event
from django.http import HttpResponse
from docx import Document
from docx.shared import Inches
from django.conf import settings
import os

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    actions = ['export_events_word']

    def export_events_word(self, request, queryset):
        # Sadece superuser kontrolü
        if not request.user.is_superuser:
            self.message_user(request, "Bu işlemi sadece admin yapabilir!", level='error')
            return None

        doc = Document()
        doc.add_heading('Events Raporu', level=1)

        for event in queryset.order_by('-date'):
            doc.add_heading(event.name, level=2)
            doc.add_paragraph(f"Tarih: {event.date.strftime('%Y-%m-%d %H:%M')}")
            doc.add_paragraph(f"Yer: {event.location}")
            doc.add_paragraph(f"Açıklama: {event.description}")

            if event.image:
                img_path = os.path.join(settings.MEDIA_ROOT, event.image.name)
                if os.path.exists(img_path):
                    try:
                        doc.add_picture(img_path, width=Inches(5))  # max genişlik 5 inch
                    except Exception as e:
                        doc.add_paragraph(f"Resim eklenemedi: {str(e)}")
                else:
                    doc.add_paragraph("Resim dosyası bulunamadı.")

            doc.add_paragraph("")  # boşluk

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename="events.docx"'
        doc.save(response)
        return response

    export_events_word.short_description = "Seçili eventleri Word olarak indir"
