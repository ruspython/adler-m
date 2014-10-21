from django.views.generic import ListView
from .models import City


class PaymentAndDeliveryView(ListView):
    model = City
    template_name = 'payment_and_delivery/payment_and_delivery.html'
    context_object_name = 'cities'