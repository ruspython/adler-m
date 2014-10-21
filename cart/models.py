from django.db import models
from django.contrib.auth.models import User
from catalog.models import Item
from django.utils.translation import ugettext_lazy as _


class Cart(models.Model):
    session = models.CharField(max_length=32, null=True, blank=True)
    date_create = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['-date_create']


class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    item = models.ForeignKey(Item)
    quantity = models.PositiveIntegerField()

    def get_price(self):
        return self.item.price

    def get_total_price(self):
        return self.get_price() * self.quantity