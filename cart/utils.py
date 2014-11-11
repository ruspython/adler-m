import random
from django.shortcuts import redirect
from .models import Cart, CartItem
from catalog.models import Item
from django.http import HttpResponse
import json


def get_current_cart(request):
    cart_id = request.COOKIES.get('cart_id', None)
    if not cart_id:
        cart_id = random.getrandbits(64)
    if request.user.is_authenticated():
        try:
            cart = Cart.objects.filter(user=request.user)[0]
        except IndexError:
            try:
                cart = Cart.objects.filter(session=cart_id)[0]
                cart.session = ''
                cart.user = request.user
            except IndexError:
                cart = Cart(user=request.user)
            cart.save()
    else:
        try:
            cart = Cart.objects.filter(user=None, session=cart_id)[0]
        except IndexError:
            cart = Cart(session=cart_id)
            cart.save()
    return cart


def add2cart(request):
    response = redirect('cart:cart')
    if request.method == 'POST':
        r_data = request.POST
    else:
        r_data = request.GET
    try:
        item = Item.objects.filter(id=r_data.get('item_id', None))[0]
        try:
            quantity = int(r_data.get('quantity', None))
            if quantity < 0:
                quantity = 1
        except (ValueError, TypeError):
            quantity = 1
        if item and quantity:
            cart = get_current_cart(request)
            response.set_cookie('cart_id', cart.session, 60*60*24*365)
            try:
                cart_item = CartItem.objects.filter(cart=cart, item=item)[0]
                cart_item.quantity += quantity
            except IndexError:
                cart_item = CartItem(
                    cart=cart,
                    item=item,
                    quantity=quantity
                )
            cart_item.save()
    except (ValueError, IndexError):
        pass

    return response


def remove_from_cart(request):
    if request.method == 'POST':
        r_data = request.POST
    else:
        r_data = request.GET

    CartItem.objects.filter(cart=get_current_cart(request), id=r_data['id']).delete()

    return redirect('cart:cart')


def cart_refresh(request):
    if request.method == 'POST':
        r_data = request.POST.dict()
    else:
        r_data = request.GET.dict()
    cart = get_current_cart(request)
    for c_id, quantity in r_data.iteritems():
        try:
            r = CartItem.objects.get(cart=cart, id=c_id)
            r.quantity = quantity
            r.save()
        except CartItem.DoesNotExist:
            pass
    data = json.dumps({
        'status': 'success'
    })
    return HttpResponse(data, mimetype='application/json')