from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(_('first name'), max_length=64, null=True, blank=True)
    second_name = models.CharField(_('second name'), max_length=64, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=64, null=True, blank=True)
    email = models.EmailField(_('email'), max_length=64, null=True, blank=True)
    zipcode = models.CharField(_('zipcode'), max_length=64, null=True, blank=True)
    city = models.CharField(_('city'), max_length=64, null=True, blank=True)
    street = models.CharField(_('street'), max_length=64, null=True, blank=True)
    house = models.CharField(_('house'), max_length=64, null=True, blank=True)
    building = models.CharField(_('building'), max_length=64, null=True, blank=True)
    apartment = models.CharField(_('apartment'), max_length=64, null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=64, null=True, blank=True)

    old_ID = models.BigIntegerField(null=True, blank=True)

    def get_full_name(self):
        return u'%s %s %s' % (self.last_name, self.first_name, self.second_name)

    def __unicode__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')