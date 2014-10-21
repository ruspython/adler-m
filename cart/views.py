from django.views.generic import ListView, View
from .models import CartItem
from django.views.decorators.csrf import csrf_exempt
from .utils import get_current_cart, add2cart, remove_from_cart, cart_refresh


class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        cart = get_current_cart(self.request)
        return super(CartView, self).get_queryset().filter(cart=cart)

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['total_weight'] = 0
        for item in context['items']:
            context['total_weight'] += item.item.weight * item.quantity
        context['total_price'] = 0
        for item in context['items']:
            context['total_price'] += item.get_price() * item.quantity
        return context


class Add2CartView(View):

    def dispatch(self, request, *args, **kwargs):
        return add2cart(request)


class CartRefreshView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return cart_refresh(request)


class RemoveFromCartView(View):

    def dispatch(self, request, *args, **kwargs):
        return remove_from_cart(request)