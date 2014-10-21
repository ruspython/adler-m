from django.conf.urls import patterns, url
from collection.views import *


urlpatterns = patterns('',
    url(r'^$', MyCollectionView.as_view(), name='my'),
    url(r'^(?P<slug>[\w]+)/$', CollectionDetailView.as_view(), name='detail'),
)