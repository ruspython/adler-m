from django.db import models
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.contrib.auth.models import User
from catalog.models import Item
from yandex_money.models import Payment


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"))
    add_time = models.DateTimeField(_('order date & time'), auto_now_add=True)

    client_name = models.CharField(_('name'), max_length=32)
    client_second_name = models.CharField(_('second name'), max_length=32, null=True, blank=True)
    client_last_name = models.CharField(_('last name'), max_length=32)

    address_city = models.CharField(_('city'), max_length=32, null=True, blank=True)
    address_street = models.CharField(_('street'), max_length=64, null=True, blank=True)
    address_house = models.CharField(_('house'), max_length=32, null=True, blank=True)
    address_building = models.CharField(_('building'), max_length=32, null=True, blank=True)
    address_flat = models.CharField(_('apt.'), max_length=32, null=True, blank=True)
    address_zipcode = models.CharField(pgettext_lazy('zipcode for order', 'zipcode'), max_length=32, null=True,
                                       blank=True)

    phone = models.CharField(_('phone'), max_length=32)
    email = models.EmailField(_('email'))

    total_price = models.PositiveIntegerField(_('total price'))
    comment = models.TextField(_('comment'), blank=True, null=True)

    order_status_choices = (
        ('new', _('new')),
        ('confirmed', _('confirmed')),
        ('shipped', _('shipped')),
    )
    delivery_method_choices = (
        ('post', _('post')),
        ('courier', _('courier')),
        ('pickup', _('pickup')),
    )
    order_status = models.CharField(_('order status'), max_length=32, choices=order_status_choices, default='new',
                                    blank=True)
    payment_status = models.BooleanField(_('payment status'), default=False)
    payment_method = models.CharField(_('payment_method'), max_length=2,
                                      choices=Payment.PAYMENT_TYPE.CHOICES, default=Payment.PAYMENT_TYPE.PC)

    delivery_method = models.CharField(_('delivery method'), max_length=32, choices=delivery_method_choices,
                                       default='post', blank=True)
    carrier = models.CharField(_('carrier'), max_length=64, null=True, blank=True, default='')

    def __unicode__(self):
        return u'%s: %s %s %s, %s' % \
               (self.add_time, self.client_name, self.client_second_name, self.client_last_name, self.total_price)

    def get_number_order(self):
        return u'%s' % (self.id, )

    get_number_order.short_description = _("order number")

    def get_client(self):
        tpl = u"""
        <big><strong>%s %s %s</strong></big>
        <div>%s</div> <div>%s</div>
        <hr>
        <div>
            <div><tt>%s %s</tt></div>
            <div><tt>%s<br></tt></div>
            <div><tt>%s %s %s</tt></div>
        </div>
        """
        return tpl % (
            self.client_last_name, self.client_name, self.client_second_name, self.email, self.phone,
            self.address_zipcode, self.address_city, self.address_street, self.address_house, self.address_building,
            self.address_flat
        )

    get_client.short_description = _("full name")
    get_client.allow_tags = True

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ['-add_time']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"))
    item = models.ForeignKey(Item, verbose_name=_("catalog item"))
    name = models.CharField(_('item name'), max_length=512)
    manufacturer = models.CharField(_('manufacturer'), max_length=64, null=True, blank=True)
    scale = models.CharField(_('scale'), max_length=64, null=True, blank=True)
    article = models.CharField(_('article'), max_length=64, null=True, blank=True)
    price = models.PositiveSmallIntegerField(_('price'))
    quantity = models.PositiveSmallIntegerField(_('quantity'), default=1)
    discount = models.FloatField(_('discount'), null=True, blank=True)

    def get_total_price(self):
        return self.price * self.quantity

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('item in order')
        verbose_name_plural = _('items in order')


