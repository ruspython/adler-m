from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', CartView.as_view(), name='cart'),
    url(r'^add/$', Add2CartView.as_view(), name='add2cart'),
    url(r'^remove/$', RemoveFromCartView.as_view(), name='remove_from_cart'),
    url(r'^refresh/$', CartRefreshView.as_view(), name='cart_refresh'),
)