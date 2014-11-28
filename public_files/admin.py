from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _


class PublicFileAdmin(admin.ModelAdmin):
    list_display = ['path', 'description']
    fieldsets = (
        (_('file'), {'fields': ['path', 'content_type', 'content', 'description']}),
    )


admin.site.register(PublicFile, PublicFileAdmin)