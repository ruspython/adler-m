from .models import Item
from django.utils.translation import ugettext_lazy as _
import re


def get_scales():
    return sorted(
        set(
            [
                item['scale']
                for item in Item.objects.values('scale').distinct()
                if item['scale']
            ]
        ),
        key=lambda x: int(re.search(':(\d+)',  x).group(1))
    )


def get_car_brands():
    return sorted(
        set(
            [
                item['brand']
                for item in Item.objects.values('brand').distinct()
                if item['brand']
            ]
        ),
    )


def get_manufacturers():
    return sorted(
        set(
            [
                item['manufacturer']
                for item in Item.objects.values('manufacturer').distinct()
                if item['manufacturer']
            ]
        )
    )


def get_car_types():
    return sorted(
        set(
            [
                item['type']
                for item in Item.objects.values('type').distinct()
                if item['type']
            ]
        ),
    )


def format_choices(choices, with_all=False):
    new_choices = [(c, c) for c in choices]
    if with_all:
        new_choices = [('', _('all'))] + new_choices
    return new_choices