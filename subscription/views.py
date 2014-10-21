from django.views.generic import TemplateView, CreateView
from .models import Subscription
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from catalog.utils import *


class MySubscriptionsView(TemplateView):
    template_name = 'subscription/subscription.html'

    def get_context_data(self, **kwargs):
        context = super(MySubscriptionsView, self).get_context_data(**kwargs)
        context['scales'] = get_scales()
        context['brands'] = get_car_brands()
        context['manufacturers'] = get_manufacturers()
        return context


class AddSubscriptionView(CreateView):
    template_name = 'subscription/create.html'
    model = Subscription

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(AddSubscriptionView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('subscription:subscription')