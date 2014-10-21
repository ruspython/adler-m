from django.db import models
from django.utils.translation import pgettext, ugettext_lazy as _
from django.contrib.auth.models import User
from catalog.models import Item
from django_resized import ResizedImageField
from django.core.urlresolvers import reverse
import random


class Collection(models.Model):
    slug = models.SlugField(_('slug'), unique=True, default=random.getrandbits(64))
    user = models.ForeignKey(User, verbose_name=_('user'))

    def __unicode__(self):
        return u'%s [%s]' % (self.user, self.code)

    def get_absolute_url(self):
        return reverse('collection_public:detail', args=[str(self.slug)])

    class Meta:
        ordering = ['slug']
        verbose_name = _('collection')
        verbose_name_plural = _('collections')


class MyCollectionItemManager(models.Manager):
    def get_queryset(self):
        return super(MyCollectionItemManager, self).get_queryset()


class CollectionItem(models.Model):
    collection = models.ForeignKey(Collection, verbose_name=_('collection'))
    catalog_product = models.ForeignKey(Item, verbose_name=_('catalog item'), null=True, blank=True)
    ordering = models.IntegerField(_('ordering'), default=100)

    objects = models.Manager()
    my_collection = MyCollectionItemManager()

    def __unicode__(self):
        return u'%s' % self.catalog_product

    class Meta:
        ordering = ['ordering']
        verbose_name = _('collection item')
        verbose_name_plural = _('collection items')


class UploadedCollectionItem(models.Model):
    collection = models.ForeignKey(Collection, verbose_name=_('collection'))
    image = ResizedImageField(_('image'), upload_to='images/collection', max_width=1000, max_height=1000, null=True, blank=True)
    name = models.CharField(pgettext('model name', 'name'), max_length=1024)
    manufacturer = models.CharField(_('manufacturer'), max_length=64)
    scale = models.CharField(_('scale'), max_length=32)
    ordering = models.IntegerField(_('ordering'), default=100)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['ordering']
        verbose_name = _('uploaded collection item')
        verbose_name_plural = _('uploaded collection items')