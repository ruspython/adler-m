from django.contrib import admin
from .models import Order, OrderItem
from django.utils.translation import ugettext_lazy as _


class OrderItemInline(admin.StackedInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_number_order', 'get_client', 'total_price', 'order_status', 'payment_method', 'payment_status']
    search_fields = ['id', 'client_name', 'client_second_name', 'client_last_name', 'address_city', 'address_street',
                     'address_house', 'address_building', 'address_flat', 'address_zipcode', 'comment', 'email',
                     'phone']
    list_filter = [
        'order_status',
        'payment_status',
    ]
    inlines = [OrderItemInline]
    fieldsets = (
        (_('Client'), {
            'fields': ('user', 'client_name', 'client_second_name', 'client_last_name', 'email', 'phone')
        }),
        (_("Address"), {
            'fields': ('address_city', 'address_street', 'address_house', 'address_building', 'address_flat',
                       'address_zipcode'),
        }),
        (_('Data of order'), {
            'fields': ('payment_method', 'total_price', 'comment',)

        }),
    )



admin.site.register(Order, OrderAdmin)