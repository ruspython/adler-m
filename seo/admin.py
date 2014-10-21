from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import SEOExtension


class SEOExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(SEOExtension, SEOExtensionAdmin)