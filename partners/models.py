from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    name = models.CharField(_('a name of city'), max_length=128)
    ordering = models.IntegerField(_('ordering'), default=10)

    def __unicode__(self):
        return u'%s' % self. name

    class Meta:
        ordering = ['ordering']
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class Partner(models.Model):
    city = models.ForeignKey(City, related_name='cities')
    name = models.CharField(_('name'), max_length=128)
    address = models.TextField(_('address'), blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=128, blank=True, null=True)
    email = models.CharField(_('email'), max_length=1024,  blank=True, null=True)
    website = models.CharField(_('website'), max_length=128, blank=True, null=True)
    ordering = models.IntegerField(_('ordering'), default=10)

    def __unicode__(self):
        return u'%s' % self. name

    class Meta:
        ordering = ['city', 'ordering']
        verbose_name = _('partner')
        verbose_name_plural = _('partners')


