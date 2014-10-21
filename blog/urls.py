from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                        url(r'^$', BlogListView.as_view(), name='article-list'),
                        url(r'^archive/$', BlogListView.as_view(), name='archive'),
                        url(r'^archive/(?P<year>\d{4})/$', BlogYearListView.as_view(), name='archive_year'),
                        url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', BlogMonthListView.as_view(),
                            name='archive_month'),
                        url(r'^(?P<slug>[\w\-]+)/$', BlogDetailView.as_view(), name='article-detail'),
                        )