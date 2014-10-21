from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.translation import ugettext_lazy as _


class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['title', 'ordering']
    list_editable = ['ordering']
    fieldsets = (
        (None, {
            'fields': ('ordering', 'image'),
        }),
        (_('titles'), {
            'fields': ('title', 'subtitle', 'color_title'),
        }),
        (_('description'), {
            'fields': ('description', 'color_description'),
        }),
        (_('button'), {
            'fields': ('button_text', 'button_link', 'color_button', 'color_button_text'),
        }),
    )


admin.site.register(Banner, BannerAdmin)
