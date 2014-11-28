from django.db import models
from django.utils.translation import ugettext_lazy as _


class PublicFile(models.Model):
    description = models.CharField(_('description'), max_length=256, null=True, blank=True,
                                   help_text=_('For example: yandex validator'))
    path = models.CharField(_('file path'), max_length=128, help_text=_('relative to the site root'))
    content_type = models.CharField(_('content_type'), max_length=128, default='text/plain')
    content = models.TextField(_('file content'), blank=True)

    def __unicode__(self):
        return self.description or self.path

    class Meta:
        ordering = ['path']
        verbose_name = _('Public file')
        verbose_name_plural = _('Public files')