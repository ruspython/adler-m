from django.contrib import admin
from .models import *


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ReviewAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]
    list_display = ['name', 'add_time', 'review']


admin.site.register(Review, ReviewAdmin)
