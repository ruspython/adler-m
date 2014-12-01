from django.db import models
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.core.urlresolvers import reverse
from django_resized import ResizedImageField
from django.core import serializers
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from itertools import chain
from cuser.middleware import CuserMiddleware


class ItemTag(models.Model):
    tag = models.CharField(_('tag'), max_length=256)

    def __unicode__(self):
        return u'%s' % self.tag

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class ItemManager(models.Manager):
    def get_queryset(self):
        return super(ItemManager, self).get_queryset().filter(quantity__gte=0)


ITEM_STATUSES = {
    'novelty': _('Novelty'),
    'pre_order': _('Pre-order'),
    'back_in_stock': _('Back in stock'),
    'sale': _('Sale'),
    'on_the_way': _('On the way'),
    'in_stock': _('In stock'),
    'few': _('Few'),
    'not_available': _('Not available'),
}


class ItemBase(models.Model):
    def __unicode__(self):
        return u'[%s] %s' % (self.article, self.name)

    def full_name(self):
        return u'%s %s' % (self.brand, self.name) if self.brand and self.section == 'model' else self.name

    @property
    def get_main_image(self):
        return self.itemimage_set.first()

    @property
    def image(self):
        return self.itemimage_set.first().file

    class Meta:
        abstract = True


class Item(ItemBase):
    ITEM_SECTIONS = (
        ('model', _('Model')),
        ('accessory', _('Accessory')),
        ('book', _('Book')),
    )
    section = models.CharField(_('section'), choices=ITEM_SECTIONS, default='model', max_length=16)
    slug = models.SlugField(_('slug'), unique=True)
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
    tags = models.ManyToManyField(ItemTag, verbose_name=_('tags'), blank=True, null=True)
    quantity = models.PositiveIntegerField(_('quantity'), null=True, blank=True)
    price = models.IntegerField(_('price'), null=True, blank=True)
    pricebeforeaction = models.IntegerField(pgettext_lazy('the price before action or sale', 'price before action'),
                                            null=True, blank=True)
    price_min = models.IntegerField(_('minimal price'), null=True, blank=True)
    new_before = models.CharField(_('new before'), max_length=256, null=True, blank=True)
    status_new = models.BooleanField(_('novelty'), default=False)
    status_not_available = models.BooleanField(_('not available'), default=False)
    status_back_in_stock = models.BooleanField(_('back in stock'), default=False)
    status_action = models.BooleanField(_('promo action'), default=False)
    status_sale = models.BooleanField(_('sale'), default=False)
    status_on_the_way = models.BooleanField(_('on the way'), default=False)
    status_without_image = models.BooleanField(_('without image'), default=False)
    is_just_updated = models.BooleanField(_('just updated'), default=False)

    objects = models.Manager()
    available = ItemManager()

    def get_article(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        if self.section == 'accessory':
            return reverse('catalog:accessory', args=[str(self.slug)])
        elif self.section == 'book':
            return reverse('catalog:book', args=[str(self.slug)])
        else:
            return reverse('catalog:item', args=[str(self.slug)])

    def get_gallery_url(self):
        return reverse('catalog:item-gallery', args=[str(self.slug)])

    def get_status(self):
        if self.status_new:
            return 'novelty'
        elif self.status_on_the_way:
            return 'pre_order'
        elif self.status_back_in_stock:
            return 'back_in_stock'
        elif self.status_action or self.status_sale:
            return 'sale'
        else:
            return None

    def get_status_string(self):
        return ITEM_STATUSES.get(self.get_status(), None)

    def get_status4cart(self):
        if self.quantity > 5:
            return 'in_stock'
        elif self.quantity > 0:
            return 'few'
        elif self.status_on_the_way:
            return 'on_the_way'
        else:
            return 'not_available'

    def get_status4cart_string(self):
        return ITEM_STATUSES.get(self.get_status4cart(), None)

    def get_properties(self):
        properties = []
        for prop in ['scale', 'brand', 'name', 'manufacturer', 'color', 'material', 'article']:
            value = getattr(self, prop)
            if value:
                properties.append({
                    'code': self._meta.get_field(prop).name,
                    'name': self._meta.get_field(prop).verbose_name.title(),
                    'value': value
                })
        return properties

    def get_similar(self):
        similar_number = 5
        items = Item.objects \
                    .filter(brand=self.brand, type=self.type) \
                    .exclude(id=self.id) \
                    .order_by('?')[:similar_number]
        if items.count() < similar_number:
            items_ext = Item.objects \
                            .filter(series=self.series) \
                            .exclude(id=self.id)[:similar_number - items.count()]
            items = list(chain(items, items_ext))
        return items

    def in_collection(self):
        user = CuserMiddleware.get_user()
        if user.is_authenticated():
            item_set = self.collectionitem_set.filter(collection__user=user)
            return item_set.count() > 0
        else:
            return False

    def get_meta_description(self):
        if self.note:
            return self.note[:160]
        else:
            return u'%s, %s, %s, %s, %s' % (
                self.scale,
                self.full_name(),
                self.manufacturer,
                self.color,
                self.material
            )

    def save(self, *args, **kwargs):
        args_dict = {}
        args_dict['item'] = self
        args_dict['item_images'] = ItemImage.objects.filter(item=self)
        response = render_to_string('admin/catalog/items_to_1C.html', args_dict)
        # print(response)
        super(Item, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('catalog item')
        verbose_name_plural = _('catalog items')
        ordering = ['id']


class ItemImage(models.Model):
    file = models.ImageField(_('image file'), upload_to='images/catalog')
    item = models.ForeignKey(Item, verbose_name=_('catalog item'))

    def __unicode__(self):
        return u'%s' % self.file.url

    def get_src(self):
        current_site = Site.objects.get_current()

        return u'%s%s' % (current_site.domain, self.file.url)

    def get_filename(self):
        return u'%s' % self.file.name.split('/')[-1]

    class Meta:
        verbose_name = _('item photo')
        verbose_name_plural = _('item photos')


class ItemType(models.Model):
    name = models.CharField(_('type'), max_length=128)
    image = models.ImageField(_('image'), upload_to='images/types')
    ordering = models.IntegerField(_('ordering'), default=100)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return u'%s?type=%s' % (reverse('catalog:item-list'), self.name)

    class Meta:
        verbose_name = _('model type')
        verbose_name_plural = _('model types')
        ordering = ['ordering']


class ImportItem(models.Model):
    uid = models.CharField(max_length=512)
    article = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    name_en = models.CharField(max_length=512)
    brand = models.CharField(max_length=512)
    brand_en = models.CharField(max_length=512)
    type = models.CharField(max_length=512)
    type_en = models.CharField(max_length=512)
    note = models.TextField()
    note_en = models.TextField()
    series = models.CharField(max_length=512)
    series_en = models.CharField(max_length=512)
    scale = models.CharField(max_length=512)
    manufacturer = models.CharField(max_length=512)
    manufacturer_en = models.CharField(max_length=512)
    color = models.CharField(max_length=512)
    color_en = models.CharField(max_length=512)
    material = models.CharField(max_length=512)
    tags = models.CharField(max_length=512)
    tags_en = models.CharField(max_length=512)
    weight = models.CharField(max_length=512)
    length = models.CharField(max_length=512)
    width = models.CharField(max_length=512)
    height = models.CharField(max_length=512)
    quantity = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    pricemin = models.CharField(max_length=512)
    publisher = models.CharField(max_length=512)
    publisher_en = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    author_en = models.CharField(max_length=512)
    statuspreorder = models.CharField(max_length=512)
    statusnew = models.CharField(max_length=512)
    statusnewavail = models.CharField(max_length=512)
    statusaction = models.CharField(max_length=512)
    statussale = models.CharField(max_length=512)
    statusway = models.CharField(max_length=512)
    statusbook = models.CharField(max_length=512)
    statusaccess = models.CharField(max_length=512)


class ImportImage(models.Model):
    item = models.ForeignKey(ImportItem)
    dir = models.CharField(max_length=1024)
    name = models.CharField(max_length=1024)
    src = models.CharField(max_length=1024)