from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                       url(r'^$', MySubscriptionsView.as_view(), name='subscription'),
                       url(r'^create/$', AddSubscriptionView.as_view(), name='create'),
                       )