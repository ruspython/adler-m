from django.views.generic import ListView, RedirectView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from catalog.models import Item
from .models import Favorite
from cart.utils import get_current_cart
from cart.models import CartItem


class FavoriteListView(ListView):
    model = Favorite
    template_name = 'favorite/cart.html'
    context_object_name = 'items'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(FavoriteListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(FavoriteListView, self).get_queryset().filter(user=self.request.user)


class Add2FavoriteView(RedirectView):
    permanent = False

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.user)
            item = Item.objects.get(id=kwargs.get('item_id'))
            Favorite.objects.get_or_create(user=user, item=item)
        except:
            pass
        return super(Add2FavoriteView, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('favorite:list')


class ActionView(RedirectView):
    permanent = False

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        items = request.POST.getlist('item', None)
        user = request.user
        r = Favorite.objects.filter(user=user, item__in=items)
        if 'remove' in request.POST:
            r.delete()
        if 'add2cart' in request.POST:
            cart = get_current_cart(request)
            for item_id in items:
                item = Item.objects.get(id=item_id)
                try:
                    cart_item = CartItem.objects.filter(cart=cart, item=item)[0]
                    cart_item.quantity += 1
                except IndexError:
                    cart_item = CartItem(
                        cart=cart,
                        item=item,
                        quantity=1
                    )
                cart_item.save()
            r.delete()
        return super(ActionView, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        if 'add2cart' in self.request.POST:
            return reverse('cart:cart')
        else:
            return reverse('favorite:list')