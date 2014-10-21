from django import template
register = template.Library()
from ..models import CartItem
from ..utils import get_current_cart


@register.inclusion_tag('cart/header_cart.html', takes_context=True)
def header_cart(context):
    return {
        'positions_count': CartItem.objects.filter(cart=get_current_cart(context['request'])).count()
    }


@register.inclusion_tag('cart/cart_info.html', takes_context=True)
def cart_info(context):
    return {
        'items': CartItem.objects.filter(cart=get_current_cart(context['request']))
    }


