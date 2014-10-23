from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
    fieldsets = (
        (_('template'), {'fields': ('name', 'slug')}),
        (_('email'), {'fields': ('recipients', 'sender', 'subject', 'template')}),
        (_('extra'), {'fields': ('description',)}),
    )


admin.site.register(EmailTemplate, EmailTemplateAdmin)