from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from .models import *


class BrandListView(ListView):
    model = Brand
    template_name = 'brands/brands.html'
    context_object_name = 'brands'


def brand_detail(request, slug):
    brand = Brand.objects.get(slug=slug)
    return render_to_response('brands/brand.html', {'brand': brand},
                              context_instance=RequestContext(request))






