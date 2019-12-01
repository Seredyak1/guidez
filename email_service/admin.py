from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import EmailTemplate


class EmailTemplateAdmin(SummernoteModelAdmin):
    list_display = ('title', 'type',)
    summernote_fields = ('body',)


admin.site.register(EmailTemplate, EmailTemplateAdmin)
