# coding: utf-8
from django.views.generic import DetailView, ListView, FormView, TemplateView
from .forms import ImportForm
from .models import *
import os
from django.conf import settings
from .xml_import import data_import
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from cart.utils import get_current_cart
from favorite.models import Favorite
from server_connect.utils import request2server
import codecs
import string
import datetime
from django.contrib.sites.models import Site


class CatalogListView(ListView):
    model = Item
    template_name = "catalog/items.html"
    context_object_name = 'items'
    paginate_by = 20
    title_ext = ''

    def get_queryset(self):
        queryset = super(CatalogListView, self).get_queryset().filter(section='model')
        get_params = self.request.GET

        q = get_params.get('q', None)
        if q:
            punc = string.punctuation
            q_list = ''.join([o for o in list(q) if not (o in punc and o != ":")]).split()
            for w in q_list:
                queryset = queryset.filter(
                    Q(name__icontains=w) |
                    Q(article__icontains=w) |
                    Q(scale=w) |
                    Q(brand=w) |
                    Q(type=w) |
                    Q(manufacturer__icontains=w) |
                    Q(color=w) |
                    Q(material=w) |
                    Q(tags__tag=w)
                )
                print(queryset)
            queryset = queryset.distinct()

        scale = get_params.get('scale', None)
        if scale:
            queryset = queryset.filter(scale=scale)
            self.title_ext += u' %s' % scale

        brand = get_params.get('brand', None)
        if brand:
            queryset = queryset.filter(brand=brand)
            self.title_ext += u' %s' % brand

        manufacturer = get_params.get('manufacturer', None)
        if manufacturer:
            queryset = queryset.filter(manufacturer=manufacturer)
            self.title_ext += u' %s' % manufacturer

        car_type = get_params.get('type', None)
        if car_type:
            queryset = queryset.filter(type=car_type)
            self.title_ext += u' %s' % car_type

        material = get_params.getlist('material', None)
        if material:
            if 'other' in material:
                all_materials = set(
                    [
                        item['material']
                        for item in Item.objects.values('material').distinct()
                        if item['material'] and item['material'] not in [u'металл', u'смола']
                    ]
                )
                material.extend(all_materials)
            queryset = queryset.filter(material__in=material)

        show_not_available = get_params.get('show_not_available', None)
        if not show_not_available:
            queryset = queryset.filter(status_not_available=False)

        tag_param = get_params.get('tag', None)
        if tag_param:
            tag = ItemTag.objects.filter(tag=tag_param)
            if tag:
                queryset = queryset.filter(tags__in=tag)
                self.title_ext += u' %s' % tag

        color = get_params.get('color', None)
        if color:
            queryset = queryset.filter(color=color)
            self.title_ext += u' %s' % color

        return queryset

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        get_params = self.request.GET
        if get_params:
            context['canonical'] = u'http://%s%s' % (
                Site.objects.get_current().domain,
                reverse('catalog:item-list')
            )
        current_tag = get_params.get('tag', None)
        if current_tag:
            context['page_header'] = _('Tag: %s') % current_tag
        context['filter_show_all'] = True
        context['title_ext'] = self.title_ext
        return context


class SearchSuggest(ListView):
    model = Item
    template_name = 'catalog/search_suggest.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super(SearchSuggest, self).get_queryset().filter(section='model')
        get_params = self.request.GET

        q = get_params.get('q', None)
        if q:
            punc = string.punctuation
            q_list = ''.join([o for o in list(q) if not (o in punc and o != ":")]).split()
            for w in q_list:
                queryset = queryset.filter(
                    Q(name__icontains=w) |
                    Q(article__icontains=w) |
                    Q(scale__icontains=w) |
                    Q(brand__icontains=w) |
                    Q(type__icontains=w) |
                    Q(manufacturer__icontains=w) |
                    Q(color__icontains=w) |
                    Q(material__icontains=w) |
                    Q(tags__tag__icontains=w)
                )
                print(queryset)
            queryset = queryset.distinct()
        return queryset[:10]


class CatalogNoveltiesView(CatalogListView):
    def get_queryset(self):
        return super(CatalogNoveltiesView, self).get_queryset().filter(status_new=True)

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['page_header'] = _('Novelties')
        context['filter_show_all'] = False
        return context


class CatalogPreOrderView(CatalogListView):
    def get_queryset(self):
        return super(CatalogPreOrderView, self).get_queryset().filter(status_on_the_way=True)
        # return super(CatalogPreOrderView, self).get_queryset().filter(
        #     Q(status_not_available=True) | Q(status_on_the_way=True)
        # )

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['page_header'] = _('Pre-order')
        context['filter_show_all'] = False
        return context


class CatalogPromoView(CatalogListView):
    def get_queryset(self):
        return super(CatalogPromoView, self).get_queryset().filter(
            Q(status_action=True) | Q(status_sale=True)
        )

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['page_header'] = _('Sale')
        context['filter_show_all'] = False
        return context


class CatalogBackInStockView(CatalogListView):
    def get_queryset(self):
        return super(CatalogBackInStockView, self).get_queryset().filter(status_back_in_stock=True)

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['page_header'] = _('Back in stock')
        context['filter_show_all'] = False
        return context


class CatalogAccessoriesListView(CatalogListView):
    def get_queryset(self):
        return Item.objects.filter(section='accessory')

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['page_header'] = _('Accessories')
        context['filter_type'] = 'accessories'
        get_params = self.request.GET
        if get_params:
            context['canonical'] = u'http://%s%s' % (
                Site.objects.get_current().domain,
                reverse('catalog:accessories')
            )
        return context


class CatalogBookListView(CatalogListView):
    def get_queryset(self):
        return Item.objects.filter(section='book')

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['page_header'] = _('Literature')
        context['filter_type'] = 'books'
        get_params = self.request.GET
        if get_params:
            context['canonical'] = u'http://%s%s' % (
                Site.objects.get_current().domain,
                reverse('catalog:books')
            )
        return context


class CatalogDetailView(DetailView):
    model = Item
    template_name = "catalog/item.html"
    context_object_name = 'item'

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        request.toolbar.populate()
        menu = request.toolbar.get_or_create_menu('catalog', _('Catalog'))
        menu.add_modal_item(
            _('Change %s') % item.name,
            url=reverse('admin:catalog_item_change', args=[item.pk])
        )
        return super(CatalogDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CatalogDetailView, self).get_context_data(**kwargs)
        cart = get_current_cart(self.request)
        item = self.get_object()
        try:
            Favorite.objects.get(user=self.request.user, item=item)
            context['in_favorite'] = True
        except:
            context['in_favorite'] = False
        context['in_cart'] = item.cartitem_set.filter(cart=cart).count() > 0
        if item.section == 'accessory':
            context['list_url'] = reverse('catalog:accessories')
        elif item.section == 'book':
            context['list_url'] = reverse('catalog:books')
        else:
            context['list_url'] = reverse('catalog:item-list')
        return context


class CatalogItemGalleryView(DetailView):
    model = Item
    template_name = "catalog/item-gallery.html"
    context_object_name = 'item'


class CatalogImportForm(FormView):
    form_class = ImportForm
    template_name = 'admin/catalog/catalog_import.html'
    success_url = 'success/'
    import_result = 'else'

    def form_valid(self, form):
        uploaded_file = self.request.FILES['file']
        upload_dir = os.path.join(settings.BASE_DIR, 'catalog_xml')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        fn = os.path.basename(uploaded_file.name)
        with open(os.path.join(upload_dir, fn), 'w+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        xml_doc = codecs.open(destination.name, 'r', 'utf-8')
        self.import_result = data_import(xml_doc.read())
        return super(CatalogImportForm, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CatalogImportForm, self).get_context_data(**kwargs)
        context['app'] = Item._meta
        context['import_result'] = self.import_result
        return context


class CatalogImportSuccess(TemplateView):
    template_name = 'admin/catalog/catalog_import_success.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogImportSuccess, self).get_context_data(**kwargs)
        context['app'] = Item._meta
        context['items_without_images'] = Item.objects.filter(status_without_image=True)
        return context


class SOAPImport(TemplateView):
    template_name = 'admin/catalog/1c_import.html'

    def dispatch(self, request, *args, **kwargs):
        return super(SOAPImport, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SOAPImport, self).get_context_data(**kwargs)
        context['app'] = Item._meta
        context['xml'] = force_text(request2server())
        context['result'] = data_import(context['xml'])
        return context


class YMLView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'catalog/yml.html'

    def get_queryset(self):
        queryset = super(YMLView, self).get_queryset()
        queryset = queryset.filter(status_not_available=False, price__isnull=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(YMLView, self).get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        context['site'] = Site.objects.get_current().domain
        return context

    def render_to_response(self, context, **response_kwargs):
        return super(YMLView, self).render_to_response(
            context,
            mimetype='application/xml',
            content_type='application/xml',
            **response_kwargs)