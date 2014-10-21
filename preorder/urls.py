from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', PreOrderListView.as_view(), name='list'),
    url(r'^add/$', Add2PreOrder.as_view(), name='add_from_form'),
    url(r'^add/(?P<item_id>\d+)/$', Add2PreOrder.as_view(), name='add'),
    url(r'^action/$', ActionView.as_view(), name='action'),
)