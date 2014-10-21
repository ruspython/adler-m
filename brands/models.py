from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField
from djangocms_text_ckeditor.fields import HTMLField
from sorl.thumbnail import get_thumbnail
from django.core.urlresolvers import reverse
from sorl.thumbnail.helpers import ThumbnailError
from cms.models.pluginmodel import CMSPlugin


class Brand(models.Model):
    name = models.CharField(_('name'), max_length=128)
    image = ResizedImageField(_('image'), max_width=1000, max_height=1000, upload_to='images/brands')
    description = HTMLField(_('description'), blank=True)
    web_site = models.CharField(_('web site'), max_length=512)
    slug = models.SlugField(_('slug'))
    ordering = models.IntegerField(_('ordering'), default=10)

    def __unicode__(self):
        return u'%s' % self. name

    def get_absolute_url(self):
        return reverse('brands:brand', args=[str(self.slug)])

    def logo_thumbnail(self):
        try:
            return '<img src="%s">' % unicode(get_thumbnail(self.image, '64x64').url)
        except ThumbnailError:
            return '<span>%s</span>' % _('no thumbnail')
    logo_thumbnail.allow_tags = True

    class Meta:
        ordering = ['ordering']
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class BrandsPluginConfig(CMSPlugin):
    label_text = models.CharField(_('label text'), max_length=128, null=True, blank=True)