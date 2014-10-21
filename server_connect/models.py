from django.db import models
from django.utils.translation import ugettext_lazy as _


class ConnectSetting(models.Model):
    key = models.CharField(_('key'), max_length=64)
    value = models.CharField(_('value'), max_length=1024)

    def __unicode__(self):
        return u'%s: %s' % (self.key, self.value)

    class Meta:
        ordering = ['key']
        verbose_name = _('setting')
        verbose_name_plural = _('connect settings')