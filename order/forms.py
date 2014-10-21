from django import forms
from .models import Order
from cuser.middleware import CuserMiddleware
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from hashlib import md5
from django.conf import settings


class OrderForm(forms.ModelForm):

    def clean_email(self):
        data = self.cleaned_data['email']
        user = CuserMiddleware.get_user()
        if not user.is_authenticated():
            try:
                User.objects.get(email=data)
                raise forms.ValidationError(_('user with this email already exists'))
            except User.MultipleObjectsReturned:
                raise forms.ValidationError(_('too many users with this email already exist'))
            except User.DoesNotExist:
                pass
        return data

    class Meta:
        model = Order
        exclude = ['user', 'total_price']