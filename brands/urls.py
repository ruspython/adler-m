from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                        url(r'^$', BrandListView.as_view(), name='brands-list'),
                        url(r'^(?P<slug>[\w\-]+)/$', 'brands.views.brand_detail', name='brand'),
                        )