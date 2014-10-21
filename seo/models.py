from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class SEOExtension(PageExtension):
    title = models.TextField(_('title'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)
    keywords = models.TextField(_('keywords'), null=True, blank=True)

    class Meta:
        verbose_name = _('SEO field')
        verbose_name_plural = _('SEO fields')




extension_pool.register(SEOExtension)