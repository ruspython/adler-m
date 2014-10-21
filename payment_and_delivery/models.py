from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from addresspicker.fields import AddressPickerField


class Country(models.Model):
    name = models.CharField(_('name'), max_length=128)
    ordering = models.IntegerField(_('ordering'), default=10)

    def __unicode__(self):
        return u'%s' % self. name

    class Meta:
        ordering = ['ordering']
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class City(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(_('name of city'), max_length=128)
    points_title = models.CharField(_('points title'), max_length=1128, blank=True, null=True)
    points = HTMLField(_('points'), blank=True)
    courier_title = models.CharField(_('courier title'), max_length=1128, blank=True, null=True)
    courier = HTMLField(_('courier'), blank=True)
    postal_title = models.CharField(_('postal title'), max_length=1128, blank=True, null=True)
    postal = HTMLField(_('postal'), blank=True)

    def __unicode__(self):
        return u'%s' % self. name

    class Meta:
        ordering = ['country', 'name']
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class PointAddress(models.Model):
    city = models.ForeignKey(City, verbose_name=_('city'))
    address = models.TextField(_('address'), max_length=512)
    map = AddressPickerField(_('place on map'), null=True, blank=True, max_length=512,
                             default='{"latlng":"0,0","zoom":5}')
    ordering = models.IntegerField(_('ordering'), default=100)

    def __unicode__(self):
        return u'%s' % self.address

    class Meta:
        verbose_name = _('point')
        verbose_name_plural = _('points')
        ordering = ['ordering']