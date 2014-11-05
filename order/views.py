import string
from django.db.models import Q
from django.views.generic import TemplateView, ListView, CreateView, FormView, DetailView
from .forms import OrderForm, ExtendedPaymentForm
from .models import Order, OrderItem
from django.core.urlresolvers import reverse
from personal.models import UserProfile
from allauth.account.views import LoginForm
from django.shortcuts import redirect
from cart.models import CartItem
from cart.utils import get_current_cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from server_connect.utils import request2server
from payment_and_delivery.models import City, PointAddress, DeliveryMethod
from adler.utils import send_sms
from adler.models import SMSMessage
from yandex_money.forms import PaymentForm
from yandex_money.models import Payment
from django.http import Http404
import re
from django.utils.translation import ugettext_lazy as _

from django import forms


class MyOrdersView(ListView):
    template_name = 'order/list.html'
    model = Order
    context_object_name = 'orders'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(MyOrdersView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(MyOrdersView, self).get_queryset().filter(user=self.request.user)


class OrderAuthView(FormView):
    template_name = 'order/auth.html'
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated() and not self.request.user.is_superuser:
            return redirect('order:create')
        return super(OrderAuthView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('order:create')

    def form_valid(self, form):
        success_url = self.get_success_url()
        return form.login(self.request, redirect_url=success_url)


class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'order/create.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(OrderCreateView, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        user = self.request.user
        if user.is_authenticated():
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            initial_data = {
                'client_name': user_profile.first_name,
                'client_second_name': user_profile.second_name,
                'client_last_name': user_profile.last_name,
                'address_zipcode': user_profile.zipcode,
                'address_city': user_profile.city,
                'address_street': user_profile.street,
                'address_house': user_profile.house,
                'address_building': user_profile.building,
                'address_flat': user_profile.apartment,
                'phone': user_profile.phone,
                'email': user_profile.email,
            }
        else:
            initial_data = None
        return initial_data

    def get_total_price(self):
        cart = get_current_cart(self.request)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = 0
        for item in cart_items:
            total_price += item.get_total_price()
        return total_price

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['total_price'] = self.get_total_price()
        return context

    def get_success_url(self, order_id=None):
        if order_id:
            return reverse('order:success_order', args=[str(order_id)])
        else:
            return reverse('order:success')

    def form_valid(self, form):
        form_data = form.save(commit=False)
        print('warning: ', self.request.POST['delivery'])
        form_data.order_status = 'new'
        form_data.delivery_method = self.request.POST['delivery']
        form_data.carrier = _('Pochta Rossii') if form_data.delivery_method == 'post' else ''
        user = self.request.user
        if not user.is_authenticated():
            new_user_password = 'password'
            User.objects.create_user(form_data.email, form_data.email, new_user_password)
            user = authenticate(username=form_data.email, password=new_user_password)
            login(self.request, user)

        cart = get_current_cart(self.request)
        cart_items = CartItem.objects.filter(cart=cart)
        form_data.user = user
        form_data.total_price = self.get_total_price()
        self.object = form.save()
        order_id = self.object.id

        # try:
        #     sms_message = SMSMessage.objects.get(slug='order_created').message % order_id
        #     send_sms(form_data.phone, sms_message)
        # except:
        #     pass

        for cart_item in cart_items:
            item = cart_item.item
            order_item = OrderItem(
                order=self.object,
                item=item,
                name=item.full_name(),
                manufacturer=item.manufacturer,
                scale=item.scale,
                article=item.get_article(),
                price=cart_item.get_price(),
                quantity=cart_item.quantity
            )
            order_item.save()
        cart_items.delete()
        return redirect(reverse("order:go_pay", args=[str(order_id)]))
        # return redirect(self.get_success_url(order_id))


class GoPayView(TemplateView):
    template_name = 'order/go_pay.html'

    def get_context_data(self, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, id=kwargs['order_id'])
        except:
            raise Http404

        phone = re.sub('[^\d^,]', '', order.phone)

        payment = Payment(
            order_amount=order.total_price,
            user=self.request.user,
            cps_email=order.email,
            cps_phone=phone
        )
        payment.save()

        context = super(GoPayView, self).get_context_data(**kwargs)
        context['order_id'] = self.kwargs.get('order_id', None)
        context['form'] = ExtendedPaymentForm(
            instance=payment,
            initial={
                'cps_email': order.email,
                'cps_phone': phone,
                'paymentType': order.payment_method
            }
        )
        return context


class GetDeliveryVariants(TemplateView):
    template_name = 'order/delivery_variants.html'

    def get_context_data(self, **kwargs):
        context = super(GetDeliveryVariants, self).get_context_data(**kwargs)
        try:
            context['city'] = City.objects.get(name=self.request.GET.get('city', None))
        except City.DoesNotExist:
            pass
        return context


class GetDirectionMap(DetailView):
    template_name = 'order/direction_map.html'
    model = PointAddress
    context_object_name = 'point'


class OrderSuccessView(TemplateView):
    template_name = 'order/success.html'

    def get_context_data(self, **kwargs):
        context = super(OrderSuccessView, self).get_context_data(**kwargs)
        context['order_id'] = self.kwargs.get('order_id', None)
        return context


class OrderPaymentSuccessView(TemplateView):
    template_name = 'order/payment_success.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPaymentSuccessView, self).get_context_data(**kwargs)
        # context['order_id'] = self.kwargs.get('order_id', None)
        return context


class OrderPaymentFailView(TemplateView):
    template_name = 'order/payment_fail.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPaymentFailView, self).get_context_data(**kwargs)
        # context['order_id'] = self.kwargs.get('order_id', None)
        return context


class CityListView(ListView):
    model = City
    template_name = 'order/city_suggest.html'
    context_object_name = 'cities'

    def get_queryset(self):
        queryset = super(CityListView, self).get_queryset().filter()
        get_params = self.request.GET

        q = get_params.get('q', None)
        if q:
            punc = string.punctuation
            q_list = ''.join([o for o in list(q) if not (o in punc and o != ":")]).split()
            for w in q_list:
                queryset = queryset.filter(
                    Q(name__icontains=w)
                )
            queryset = queryset.distinct()
        return queryset[:10]


class DeliveryMethodListView(ListView):
    model = DeliveryMethod
    template_name = 'order/delivery_method_suggest.html'
    context_object_name = 'methods'

    def get_queryset(self):
        queryset = super(DeliveryMethodListView, self).get_queryset().filter()
        get_params = self.request.GET

        city_name = get_params.get('city', None)
        if city_name:
            city = City.objects.get(name=city_name)
            queryset = city.delivery_method.all()
        return queryset