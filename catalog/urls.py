from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                        url(r'^$', CatalogListView.as_view(), name='item-list'),
                        url(r'^suggest/$', SearchSuggest.as_view(), name='suggest'),
                        url(r'^yml\.asm$', YMLView.as_view(), name='yml'),
                        url(r'^new/$', CatalogNoveltiesView.as_view(), name='novelties'),
                        url(r'^pre-order/$', CatalogPreOrderView.as_view(), name='pre-order'),
                        url(r'^sale/$', CatalogPromoView.as_view(), name='sale'),
                        url(r'^back-in-stock/$', CatalogBackInStockView.as_view(), name='back-in-stock'),
                        url(r'^books/$', CatalogBookListView.as_view(), name='books'),
                        url(r'^books/(?P<slug>[^/]+)/$', CatalogDetailView.as_view(), name='book'),
                        url(r'^accessories/$', CatalogAccessoriesListView.as_view(), name='accessories'),
                        url(r'^accessories/(?P<slug>[^/]+)/$', CatalogDetailView.as_view(), name='accessory'),
                        url(r'^(?P<slug>[^/]+)/$', CatalogDetailView.as_view(), name='item'),
                        url(r'^gallery/(?P<slug>[^/]+)/$', CatalogItemGalleryView.as_view(), name='item-gallery'),
                        )