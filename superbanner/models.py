from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField


class Banner(models.Model):
    color_help = _('for example: #ff5b2d, rgb(255,91,45), red.'
                   '<a target="_blank" href="http://htmlbook.ru/css/value/color">Documentation</a>')
    image = ResizedImageField(_('image'), max_width=1000, max_height=1000, upload_to='images/banner')
    title = models.CharField(_('title'), max_length=128)
    subtitle = models.CharField(_('subtitle'), max_length=128, null=True, blank=True)
    color_title = models.CharField(_('color title'), max_length=16, null=True, blank=True, help_text=color_help)
    description = models.TextField(_('description'), blank=True, null=True)
    color_description = models.CharField(_('color description'), max_length=16, blank=True, null=True,
                                         help_text=color_help)
    button_text = models.CharField(_('text on button'), max_length=128, null=True, blank=True)
    button_link = models.CharField(_('link from button'), max_length=1024, null=True, blank=True)
    color_button = models.CharField(_('color button'), max_length=16, blank=True, null=True, help_text=color_help)
    color_button_text = models.CharField(_('color button text'), max_length=16, blank=True, null=True,
                                         help_text=color_help)
    ordering = models.IntegerField(_('ordering'), default=10)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['ordering']
        verbose_name = _('banner')
        verbose_name_plural = _('banners')

