from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', FavoriteListView.as_view(), name='list'),
    url(r'^add/(?P<item_id>[\d]+)/$', Add2FavoriteView.as_view(), name='add'),
    url(r'^action/$', ActionView.as_view(), name='action'),
)