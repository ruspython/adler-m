from django.contrib import admin
from .models import *


class BrandAdmin(admin.ModelAdmin):
    list_display = ['logo_thumbnail', 'name', 'slug', 'ordering']
    list_display_links = ['name']
    list_editable = ['ordering', 'slug']


admin.site.register(Brand, BrandAdmin)
