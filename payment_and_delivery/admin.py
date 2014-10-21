from django.contrib import admin
from .models import *
from cms.admin.placeholderadmin import PlaceholderAdmin
from django.utils.translation import ugettext_lazy as _


class PointsInline(admin.StackedInline):
    model = PointAddress


class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ['country']
    fieldsets = (
        (None, {
            'fields': ('country', 'name')
        }),
        (_('points'), {
            'fields': ('points_title', 'points')
        }),
        (_('courier'), {
            'classes': ('wide',),
            'fields': ('courier_title', 'courier')
        }),
        (_('postal'), {
            'classes': ('extrapretty',),
            'fields': ('postal_title', 'postal')
        }),
    )
    inlines = [PointsInline]


admin.site.register(Country, PlaceholderAdmin)
admin.site.register(City, CityAdmin)
