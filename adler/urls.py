from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from order.views import OrderPaymentSuccessView, OrderPaymentFailView
from cms.sitemaps import CMSSitemap

admin.autodiscover()


urlpatterns = i18n_patterns('',
                            url(r'^personal/orders/error/$', OrderPaymentFailView.as_view(),
                                name='payment_fail'),
                            url(r'^personal/orders/success/$', OrderPaymentSuccessView.as_view(),
                                name='payment_success'),
                            url(r'^api/pay/test/', include('yandex_money.urls')),
                            url(r'^api/', include('server_connect.urls')),
                            url(r'^admin/', include(admin.site.urls)),
                            url(r'^ckeditor/', include('ckeditor.urls')),
                            url(r'^accounts/', include('allauth.urls')),
                            url(r'^collection/', include('collection_public.urls', namespace='collection_public')),
                            # url(r'^personal/pre-order/', include('preorder.urls', namespace='preorder')),
                            url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                                {'sitemaps': {'cmspages': CMSSitemap}}),
                            url(r'^', include('cms.urls')),
                            )

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           ) + staticfiles_urlpatterns() + urlpatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )