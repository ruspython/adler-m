from django.views.generic import ListView
from .models import *


class PartnerListView(ListView):
    model = Partner
    template_name = 'partners/partners.html'
    context_object_name = 'partners'