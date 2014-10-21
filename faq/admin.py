from django.contrib import admin
from .models import *


class FaqAdmin(admin.ModelAdmin):
    list_display = ['name', 'question', 'ordering']
    list_display_links = ['name', 'question']
    list_editable = ['ordering']


admin.site.register(Faq, FaqAdmin)