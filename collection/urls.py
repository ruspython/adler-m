from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', MyCollectionView.as_view(), name='my'),
    url(r'^add/(?P<pk>[\d]+)/$', Add2Collection.as_view(), name='add'),
    url(r'^create/$', CreateCollectionItemView.as_view(), name='create'),
    url(r'^update/(?P<pk>[\d]+)/$', UpdateCollectionItemView.as_view(), name='update'),
    url('^remove/(?P<pk>[\d]+)/$', DeleteItem.as_view(), name='remove'),
    url('^remove_uploaded/(?P<pk>[\d]+)/$', DeleteUploadedItem.as_view(), name='remove_uploaded'),
)