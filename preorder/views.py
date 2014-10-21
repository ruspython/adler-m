from django.views.generic import ListView, RedirectView
from .models import PreOrder
from catalog.models import Item
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse


class PreOrderListView(ListView):
    model = PreOrder
    template_name = 'preorder/list.html'
    context_object_name = 'items'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(PreOrderListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(PreOrderListView, self).get_queryset().filter(user=self.request.user)


class Add2PreOrder(RedirectView):
    permanent = False

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            item_id = request.POST.get('item_id', None)
            quantity = int(request.POST.get('quantity', None))
        else:
            item_id = kwargs.get('item_id', None)
            quantity = 1
        try:
            user = User.objects.get(username=request.user)
            item = Item.objects.get(id=item_id)
            preorder, created = PreOrder.objects.get_or_create(user=user, item=item)
            if created:
                preorder.quantity = quantity
            else:
                preorder.quantity += quantity
            preorder.save()
        except:
            pass
        return super(Add2PreOrder, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('preorder:list')


class ActionView(RedirectView):
    permanent = False

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        items = request.POST.getlist('item', None)
        user = request.user
        r = PreOrder.objects.filter(user=user, item__in=items)
        if 'cancel' in request.POST:
            r.delete()
        return super(ActionView, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('preorder:list')