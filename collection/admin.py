from django.contrib import admin
from .models import Collection, CollectionItem, UploadedCollectionItem


class CollectionItemInline(admin.TabularInline):
    model = CollectionItem


class UploadedCollectionItemInline(admin.TabularInline):
    model = UploadedCollectionItem


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['slug', 'user']
    inlines = [CollectionItemInline, UploadedCollectionItemInline]


admin.site.register(Collection, CollectionAdmin)