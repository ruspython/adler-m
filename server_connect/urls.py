from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^import_request/$', ImportRequest.as_view(), name='import_request'),
)