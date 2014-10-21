from django.conf.urls import patterns, url
from .views import *
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', ReviewListView.as_view(), name='reviews'),
    url(r'^add/$', ReviewCreateView.as_view(), name='create_review'),
    url(r'^review_add_success/$',
        TemplateView.as_view(template_name='reviews/review_success.html'),
        name='review_add_success'),
    url(r'^add_comment/$', CommentCreateView.as_view(), name='add_comment'),
    url(r'^add_comment/(?P<pk>[\d]+)/$', CommentCreateView.as_view(), name='create_comment'),
    url(r'^comment_add_success/$',
        TemplateView.as_view(template_name='reviews/review_success.html'),
        name='comment_add_success'),
)