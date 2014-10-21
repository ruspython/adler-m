from django.db import models
from django.utils.translation import ugettext_lazy as _
from addresspicker.fields import AddressPickerField


class Contact(models.Model):
    name = models.CharField(_('name'), max_length=64)
    ordering = models.IntegerField(_('ordering'), default=100)
    description = models.TextField(_('description'), null=True, blank=True)
    use_map = models.BooleanField(_('use map'), default=False)
    show_immediately = models.BooleanField(_('show immediately'), default=True)
    map = AddressPickerField(_('place on map'), max_length=128, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['ordering']
        verbose_name = _('contact entry')
        verbose_name_plural = _('contact entries')


class Feedback(models.Model):
    CITY_CHOICES = (
        ('spb', _('St petersburg')),
        ('msk', _('Moscow')),
        ('other', _('Other city')),
    )
    DEPARTMENT_CHOICES = (
        ('wholesale', _('wholesale')),
        ('retail', _('retail')),
    )
    add_time = models.DateTimeField(_('add time'), auto_now_add=True)
    name = models.CharField(_('your name'), max_length=128)
    city = models.CharField(_('your city'), max_length=16, choices=CITY_CHOICES, default='spb')
    contact = models.CharField(_('phone or email'), max_length=256, blank=True, null=True)
    department = models.CharField(_('department'), max_length=16, choices=DEPARTMENT_CHOICES, default='wholesale')
    message = models.TextField(_('message'))

    def __unicode__(self):
        return u'%s: %s, %s' % (self.add_time, self.name, self.city)

    class Meta:
        ordering = ['-add_time']
        verbose_name = _('message')
        verbose_name_plural = _('messages')