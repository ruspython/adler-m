from django.db import models
from django.utils.translation import pgettext, ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from catalog.models import Item, ItemBase
import datetime
from itertools import chain
from django_resized import ResizedImageField


class BlogTag(models.Model):
    tag = models.CharField(_('tag'), max_length=256, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.tag

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogUploadedModel(ItemBase):
    article = models.CharField(_('article'), max_length=64)
    name = models.CharField(_('model name'), max_length=512)
    brand = models.CharField(_('model brand'), max_length=512, null=True, blank=True)
    type = models.CharField(_('model type'), max_length=512, null=True, blank=True)
    comment = models.TextField(_('comment'), null=True, blank=True)
    note = models.TextField(_('note'), null=True, blank=True)
    series = models.CharField(_('series'), max_length=512, null=True, blank=True)
    scale = models.CharField(_('scale'), max_length=32, null=True, blank=True)
    manufacturer = models.CharField(_('manufacturer'), max_length=256, null=True, blank=True)
    color = models.CharField(_('color'), max_length=256, null=True, blank=True)
    material = models.CharField(_('material'), max_length=256, null=True, blank=True)
    weight = models.FloatField(_('weight'), null=True, blank=True)
    length = models.CharField(_('length'), max_length=256, null=True, blank=True)
    width = models.CharField(_('width'), max_length=256, null=True, blank=True)
    height = models.CharField(_('height'), max_length=256, null=True, blank=True)
    price = models.IntegerField(_('price'), null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    @property
    def get_main_image(self):
        return self.bloguploadedmodelimage_set.first()

    @property
    def image(self):
        return self.bloguploadedmodelimage_set.first().file

    @property
    def section(self):
        return "model"

    def get_gallery_url(self):
        return None

    class Meta:
        verbose_name = _('uploaded model')
        verbose_name_plural = _('uploaded models')


class BlogUploadedModelImage(models.Model):
    file = ResizedImageField(_('image file'), max_width=1020, max_height=1000, upload_to='images/blog')
    item = models.ForeignKey(BlogUploadedModel, verbose_name=_('catalog item'))

    def __unicode__(self):
        return u'%s' % self.file.url

    class Meta:
        verbose_name = _('item photo')
        verbose_name_plural = _('item photos')


class Blog(models.Model):
    slug = models.SlugField(_('slug'), unique=True)
    date = models.DateField(_('date'), default=datetime.date.today(), blank=True, null=True)
    title = models.CharField(_('title'), max_length=1280)
    announce = models.TextField(_('announce'), blank=True, null=True, max_length=256)
    text = RichTextField(_('text'), blank=True, null=True)
    tags = models.ManyToManyField(BlogTag, verbose_name=_('tags'), blank=True, null=True)
    item = models.ManyToManyField(Item, verbose_name=pgettext('catalog items', 'items'), blank=True, null=True)
    uploaded_item = models.ManyToManyField(BlogUploadedModel,
                                           verbose_name=_('uploaded items'),
                                           related_name='uploaded',
                                           blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[str(self.slug)])

    def get_all_tags(self):
        self_tags = list(self.tags.all())
        for item in self.item.all():
            for tag in item.tags.all():
                if not tag in self_tags:
                    self_tags.append(tag)
        return self_tags

    def get_image(self):
        main_image = None
        catalog_items = self.item.all()
        uploaded_items = self.uploaded_item.all()
        if catalog_items.count() > 0:
            first_item_images = catalog_items.first().itemimage_set.all()
            if first_item_images.count() > 0:
                main_image = first_item_images.first().file
        elif uploaded_items.count() > 0:
            first_item_images = uploaded_items.first().bloguploadedmodelimage_set.all()
            if first_item_images.count() > 0:
                main_image = first_item_images.first().file

        return main_image

    def get_item_list(self):
        catalog_items = self.item.all()
        uploaded_items = self.uploaded_item.all()
        result = list(chain(catalog_items, uploaded_items))
        return result

    def get_related_articles(self):
        return Blog.objects.exclude(pk=self.pk).order_by("?")[:2]

    class Meta:
        ordering = ['-date']
        verbose_name = pgettext('Blog article', 'article')
        verbose_name_plural = pgettext('Blog articles', 'articles')



