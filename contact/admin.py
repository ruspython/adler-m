from django.contrib import admin
from .models import *


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['add_time', 'name', 'city']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'ordering', 'use_map', 'show_immediately']
    list_editable = ['ordering', 'use_map', 'show_immediately']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)