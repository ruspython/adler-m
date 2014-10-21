from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', ProfileUpdate.as_view(), name='profile'),
    url(r'^delete/$', ProfileDeleteView.as_view(), name='profile_delete_confirm'),
    url(r'^delete/do/$', ProfileDelete.as_view(), name='profile_delete'),
)