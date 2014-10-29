from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                       url(r'^$', MyOrdersView.as_view(), name='list'),
                       url(r'get_city/$', CityListView.as_view(), name='get_cities'),
                       url(r'get_delivery_method/$', DeliveryMethodListView.as_view(), name='get_delivery_methods'),
                       url(r'make/$', OrderCreateView.as_view(), name='create'),
                       url(r'make/auth/$', OrderAuthView.as_view(), name='auth'),
                       url(r'make/go_pay/(?P<order_id>[\d]+)/$', GoPayView.as_view(), name='go_pay'),
                       url(r'success/$', OrderSuccessView.as_view(), name='success'),
                       url(r'success/(?P<order_id>[\d]+)/$', OrderSuccessView.as_view(), name='success_order'),
                       url(r'get_delivery_variants/$', GetDeliveryVariants.as_view(), name='get_delivery_variants'),
                       url(r'get_direction_map/(?P<pk>[\d]+)/$', GetDirectionMap.as_view(),
                           name='get_direction_map'),
                       )