from django.contrib import admin
from .models import *
from .views import *
from sorl.thumbnail.admin import AdminImageMixin
from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from adler.utils import TranslationTabMixin


class ItemImageInline(AdminImageMixin, admin.TabularInline):
    model = ItemImage


class ItemAdmin(TranslationTabMixin, AdminImageMixin, admin.ModelAdmin):
    list_display = ['slug', 'name', 'price', 'quantity']
    list_editable = ['price', 'quantity']
    list_filter = [
        'scale',
        # 'color',
        # 'manufacturer',
        # 'tags',
        'brand',
        'type',
        'series',
        'material',
        'status_new',
        'status_not_available',
        'status_back_in_stock',
        'status_action',
        'status_sale',
        'status_on_the_way',
    ]
    search_fields = ['name', 'slug']
    inlines = [ItemImageInline]
    filter_horizontal = ['tags']
    fieldsets = (
        (None, {
            'fields': ('name', 'section', 'slug'),
        }),
        (None, {'fields': ('article', 'comment', 'note')}),
        (_('characteristics'), {
            'fields': ('brand', 'type', 'series', 'scale', 'manufacturer',
                       'color', 'material', 'weight', 'length', 'width', 'height')
        }),
        (_('tags'), {'fields': ('tags',), 'classes': ('collapse',)}),
        (_('catalog'), {'fields': ('price', 'pricebeforeaction', 'price_min', 'quantity')}),
        (_('statuses'), {
            'fields': ('new_before', 'status_new', 'status_not_available', 'status_back_in_stock', 'status_action',
                       'status_sale', 'status_on_the_way'),
            'classes': ('collapse',)
        })
    )

    class Media:
        css = {
            "all": ("catalog/admin.css",)
        }

    def get_urls(self):
        urls = super(ItemAdmin, self).get_urls()
        extra_urls = patterns('',
                              url(r'^import/$', self.admin_site.admin_view(CatalogImportForm.as_view()),
                                  name='xml_import'),
                              url(r'^import/success/$', self.admin_site.admin_view(CatalogImportSuccess.as_view()),
                                  name='xml_import_success'),
                              url(r'^request2server/$', self.admin_site.admin_view(SOAPImport.as_view()),
                                  name='soap_import'),
                              url(r'^(?P<pk>\d+)/update/$', self.admin_site.admin_view(ItemUpdate.as_view()),
                                  name='item_update'),
                              )
        return extra_urls + urls


class ItemTypeAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(ItemTag)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)