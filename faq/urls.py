from django.conf.urls import patterns, url
from .views import *
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', FaqListView.as_view()),
    url(r'^add/$', FaqCreateView.as_view(), name='create_faq'),
    url(r'^faq_add_success/$',
        TemplateView.as_view(template_name='faq/faq_success.html'),
        name='faq_add_success'),
)