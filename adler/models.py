from django.db import models
from django.utils.translation import ugettext_lazy as _


class SMSMessage(models.Model):
    slug = models.SlugField(_('slug'), unique=True)
    description = models.CharField(_('description'), max_length=512)
    message = models.TextField(_('message text'))

    def __unicode__(self):
        return u'%s' % self.description

    class Meta:
        verbose_name = _('SMS Message')
        verbose_name_plural = _('SMS Messages')