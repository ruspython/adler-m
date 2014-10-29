from django.contrib import admin
from .models import *


class PartnerInline(admin.TabularInline):
    model = Partner

    # def get_formset(self, request, obj=None, **kwargs):
    #     self.max_num = obj.model.port_count
    #     return super(PartnerInline, self).get_formset(request, obj, **kwargs)


class CityAdmin(admin.ModelAdmin):
    inlines = [PartnerInline, ]
    list_display = ['name', 'ordering']
    list_editable = ['ordering']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'ordering']
    list_editable = ['ordering']


admin.site.register(City, CityAdmin)
admin.site.register(Partner, PartnerAdmin)
