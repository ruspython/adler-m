from django.db import models
from django.utils.translation import ugettext_lazy as _
from catalog.models import Item
from django.contrib.auth.models import User


class PreOrder(models.Model):
    item = models.ForeignKey(Item, verbose_name=_('catalog item'))
    user = models.ForeignKey(User, verbose_name=_('user'))
    add_time = models.DateTimeField(_('add time'), auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(_('quantity'), default=1)

    def __unicode__(self):
        return u'%s' % self.item.name

    class Meta:
        verbose_name = _('pre-order item')
        verbose_name_plural = _('pre-order items')
        ordering = ['add_time']