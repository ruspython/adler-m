from django.contrib import admin
from .models import *
from adler.utils import TranslationTabMixin
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin


class BlogAdmin(TranslationTabMixin, admin.ModelAdmin):
    list_display = ['date', 'title', 'slug']
    list_display_links = ['title']
    list_editable = ['slug']
    fieldsets = (
        # (_('tags'), {'fields': ('tags',), 'classes': ('collapse',)})
    )
    filter_horizontal = ['item', 'uploaded_item']


class TagAdmin(admin.ModelAdmin):
    pass


class BlogUploadedModelImageInline(AdminInlineImageMixin, admin.TabularInline):
    model = BlogUploadedModelImage


class BlogUploadedModelAdmin(TranslationTabMixin, AdminImageMixin, admin.ModelAdmin):
    inlines = [BlogUploadedModelImageInline]


admin.site.register(BlogUploadedModel, BlogUploadedModelAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogTag, TagAdmin)