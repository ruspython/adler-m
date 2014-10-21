from django import forms
from django.utils.translation import ugettext_lazy as _
from .utils import *


class ImportForm(forms.Form):
    file = forms.FileField()


class AccessoriesForm(forms.Form):
    scale = forms.ChoiceField(label=_('Scale'), choices=format_choices(get_scales(), True), required=False)
    type = forms.ChoiceField(label=_('Type'), choices=format_choices(get_car_types(), True), required=False)
    manufacturer = forms.ChoiceField(label=_('Manufacturer'), choices=format_choices(get_manufacturers(), True),
                                     required=False)


class LiteratureFilterForm(forms.Form):
    catalogues = forms.BooleanField(label=_('Catalogues'))
    magazines = forms.BooleanField(label=_('Magazines'))
    books = forms.BooleanField(label=_('Books'))


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label=_('Search'))