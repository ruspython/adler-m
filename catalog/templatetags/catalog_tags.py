# coding: utf-8
from django import template
register = template.Library()
from ..models import Item
# import re
from ..utils import *
from ..forms import LiteratureFilterForm, AccessoriesForm, SearchForm


@register.inclusion_tag('catalog/catalog_filter.html', takes_context=True)
def catalog_filter(context, show_all=True):
    materials = [
        u'металл',
        u'смола',
    ]

    request = context['request']
    filter_values = {
        'scale': request.GET.get('scale', None),
        'brand': request.GET.get('brand', None),
        'manufacturer': request.GET.get('manufacturer', None),
        'type': request.GET.get('type', None),
        'material': request.GET.getlist('material', None),
        'show_not_available': request.GET.get('show_not_available', None),
    }

    return {
        'scales': get_scales(),
        'car_brands': get_car_brands(),
        'manufacturers': get_manufacturers(),
        'car_types': get_car_types(),
        'materials': materials,
        'filter_values': filter_values,
        'filter_show_all': show_all,
        'q': request.GET.get('q', None),
    }


@register.inclusion_tag('catalog/accessories_filter.html', takes_context=True)
def accessories_filter(context):
    form = AccessoriesForm(context['request'].GET)
    return {'form': form}


@register.inclusion_tag('catalog/books_filter.html', takes_context=True)
def books_filter(context):
    form = LiteratureFilterForm(context['request'].GET)
    return {'form': form}


@register.inclusion_tag('catalog/search_form.html', takes_context=True)
def search_form(context):
    return {'form': SearchForm(context['request'].GET)}