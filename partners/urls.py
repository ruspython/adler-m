from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                        url(r'^$', PartnerListView.as_view(), name='partners'),
                        )