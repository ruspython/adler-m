from .models import Item, ItemImage, ItemTag, ImportItem, ImportImage
import xml.etree.cElementTree as eTree
from django.conf import settings
import os.path
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from slugify import UniqueSlugify


def save_image_from_url(model, url, filename):
    r = requests.get(url)

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(r.content)
    img_temp.flush()

    model.image.save(filename, File(img_temp), save=True)


def load_images_for_item():
    pass


def data_import(xml_doc_data):
    img_dir = 'images/catalog/'

    xml_doc_tree = eTree.fromstring(xml_doc_data.encode('utf-8'))

    def to_int(s):
        try:
            return int(float(s))
        except:
            return None

    def to_boolean(s):
        try:
            return True if s.lower() == 'true' else False
        except:
            return False

    for item in xml_doc_tree.iter('nomen-item'):
        article = item.attrib.get('id', None)
        slugify_unique = UniqueSlugify(separator='_')
        slug = slugify_unique(article)
        if article:
            new_item, created = Item.objects.get_or_create(slug=slug)
            if to_boolean(item.attrib.get('statusaccess', None)):
                section = 'accessory'
            elif to_boolean(item.attrib.get('statusbook', None)):
                section = 'book'
            else:
                section = 'model'
            item_info = {
                'article': article,
                'section': section,
                'name': item.attrib.get('name', None),
                'name_en': item.attrib.get('name_en', None),
                'brand': item.attrib.get('brand', None),
                'brand_en': item.attrib.get('brand_en', None),
                'type': item.attrib.get('type', None),
                'type_en': item.attrib.get('type_en', None),
                'comment': item.attrib.get('comment', None),
                'comment_en': item.attrib.get('comment_en', None),
                'note': item.attrib.get('note', None),
                'note_en': item.attrib.get('note_en', None),
                'series': item.attrib.get('series', None),
                'series_en': item.attrib.get('series_en', None),
                'scale': item.attrib.get('scale', None),
                'manufacturer': item.attrib.get('manufacturer', None),
                'manufacturer_en': item.attrib.get('manufacturer_en', None),
                'color': item.attrib.get('color', None),
                'color_en': item.attrib.get('color_en', None),
                'material': item.attrib.get('material', None),
                'weight': item.attrib.get('weight', None),
                'length': item.attrib.get('length', None),
                'width': item.attrib.get('width', None),
                'height': item.attrib.get('height', None),
                'quantity': to_int(item.attrib.get('quantity', 0)),
                'price': to_int(item.attrib.get('price', None)),
                'price_min': to_int(item.attrib.get('pricemin', None)),
                'new_before': item.attrib.get('newbefore', None),
                'status_new': to_boolean(item.attrib.get('statusnew', None)),
                'status_not_available': to_boolean(item.attrib.get('statusnotavail', None)),
                'status_back_in_stock': to_boolean(item.attrib.get('statusnewavail', None)),
                'status_action': to_boolean(item.attrib.get('statusaction', None)),
                'status_sale': to_boolean(item.attrib.get('statussale', None)),
                'status_on_the_way': to_boolean(item.attrib.get('statusway', None))
            }
            for (key, value) in item_info.items():
                setattr(new_item, key, value)

            tags = item.attrib.get('tags', '').split(';')
            for tag in tags:
                tag = tag.strip()
                if tag:
                    try:
                        db_tag = ItemTag.objects.get(tag=tag)
                    except ItemTag.DoesNotExist:
                        db_tag = ItemTag(tag=tag)
                        db_tag.save()
                    new_item.tags.add(db_tag)

    #         image_count = 0
    #         for image in item.iter('img'):
    #             file_src = image.attrib.get('src', None)
    #             file_name = image.attrib.get('name', None)
    #             if file_src:
    #                 # save_image_from_url(Item, file_src, file_name)
    #                 r = requests.get(file_src)
    #
    #                 img_temp = NamedTemporaryFile(delete=True)
    #                 img_temp.write(r.content)
    #                 img_temp.flush()
    #
    # # model.image.save(filename, File(img_temp), save=True)
    #                 file_path = os.path.join(img_dir, image.attrib.get('dir', None), image.attrib.get('name', None))
    # #             if os.path.isfile(os.path.join(settings.MEDIA_ROOT, file_path)):
    #                 new_image = ItemImage(
    #                     file=File(img_temp, file_path),
    #                     item=new_item
    #                 )
    #                 new_image.save()
    #                 print('Image imported: ', new_image)
    #                 image_count += 1
    #         if image_count <= 0:
    #             new_item.status_without_image = True
            new_item.is_just_updated = True
            new_item.save()
            print('Item imported: ', new_item)


def read_catalog_data(xml_doc_data):
    # xml_doc_tree = eTree.fromstring(xml_doc_data.encode('utf-8'))
    xml_doc_tree = eTree.fromstring(xml_doc_data)
    ImportItem.objects.all().delete()
    ImportImage.objects.all().delete()
    for item in xml_doc_tree.iter('nomen-item'):
        article = item.attrib.get('id', None)
        new_import_item = ImportItem(
            uid=item.attrib.get('uid', None),
            article=article,
            name=item.attrib.get('name', None),
            name_en=item.attrib.get('name_en', None),
            brand=item.attrib.get('brand', None),
            brand_en=item.attrib.get('brand_en', None),
            type=item.attrib.get('type', None),
            type_en=item.attrib.get('type_en', None),
            note=item.attrib.get('note', None),
            note_en=item.attrib.get('note_en', None),
            series=item.attrib.get('series', None),
            series_en=item.attrib.get('series_en', None),
            scale=item.attrib.get('scale', None),
            manufacturer=item.attrib.get('manufacturer', None),
            manufacturer_en=item.attrib.get('manufacturer_en', None),
            color=item.attrib.get('color', None),
            color_en=item.attrib.get('color_en', None),
            material=item.attrib.get('material', None),
            tags=item.attrib.get('tags', None),
            tags_en=item.attrib.get('tags_en', None),
            weight=item.attrib.get('weight', None),
            length=item.attrib.get('length', None),
            width=item.attrib.get('width', None),
            height=item.attrib.get('height', None),
            quantity=item.attrib.get('quantity', None),
            price=item.attrib.get('price', None),
            pricemin=item.attrib.get('pricemin', None),
            publisher=item.attrib.get('publisher', None),
            publisher_en=item.attrib.get('publisher_en', None),
            author=item.attrib.get('author', None),
            author_en=item.attrib.get('author_en', None),
            statuspreorder=item.attrib.get('statuspreorder', None),
            statusnew=item.attrib.get('statusnew', None),
            statusnewavail=item.attrib.get('statusnewavail', None),
            statusaction=item.attrib.get('statusaction', None),
            statussale=item.attrib.get('statussale', None),
            statusway=item.attrib.get('statusway', None),
            statusbook=item.attrib.get('statusbook', None),
            statusaccess=item.attrib.get('statusaccess', None),
        )
        new_import_item.save()
        for image in item.iter('img'):
            new_import_image = ImportImage(
                item=new_import_item,
                dir=image.attrib.get('dir', None),
                name=image.attrib.get('name', None),
                src=image.attrib.get('src', None),
            )
            new_import_image.save()


def import_item_from_tmp(item):
    img_dir = 'images/catalog/'
    slugify_unique = UniqueSlugify(separator='_')
    slug = slugify_unique(item.article)
    print(slug)

    def to_int(s):
        try:
            return int(float(s))
        except:
            return None

    def to_boolean(s):
        try:
            return True if s.lower() == 'true' else False
        except:
            return False

    def to_str(s):
        try:
            return s.encode('utf-8')
        except:
            return ''

    if slug:
        new_item, created = Item.objects.get_or_create(slug=slug)
        if to_boolean(item.statusaccess):
            section = 'accessory'
        elif to_boolean(item.statusbook):
            section = 'book'
        else:
            section = 'model'
        item_info = {
            'article': to_str(item.article),
            'section': section,
            'name': to_str(item.name),
            'name_en': to_str(item.name_en),
            'brand': to_str(item.brand),
            'brand_en': to_str(item.brand_en),
            'type': to_str(item.type),
            'type_en': to_str(item.type_en),
            'note': to_str(item.note),
            'note_en': to_str(item.note_en),
            'series': to_str(item.series),
            'series_en': to_str(item.series_en),
            'scale': item.scale,
            'manufacturer': to_str(item.manufacturer),
            'manufacturer_en': to_str(item.manufacturer_en),
            'color': to_str(item.color),
            'color_en': to_str(item.color_en),
            'material': to_str(item.material),
            'weight': item.weight,
            'length': item.length,
            'width': item.width,
            'height': item.height,
            'quantity': to_int(item.quantity),
            'price': to_int(item.price),
            'price_min': to_int(item.pricemin),
            'status_new': to_boolean(item.statusnew),
            'status_back_in_stock': to_boolean(item.statusnewavail),
            'status_action': to_boolean(item.statusaction),
            'status_sale': to_boolean(item.statussale),
            'status_on_the_way': to_boolean(item.statusway)
        }
        print(item.name.encode('utf-8'))
        for (key, value) in item_info.items():
            setattr(new_item, key, value)
        # print(item_info)

        tags = item.tags.split(';')
        for tag in tags:
            tag = tag.strip()
            if tag:
                try:
                    db_tag = ItemTag.objects.get(tag=tag)
                except ItemTag.DoesNotExist:
                    db_tag = ItemTag(tag=tag)
                    db_tag.save()
                new_item.tags.add(db_tag)

        image_count = 0
        for image in item.importimage_set.all():
            if image.src:
                r = requests.get(image.src)

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(r.content)
                img_temp.flush()

                file_path = os.path.join(img_dir, image.dir, image.name)
                if not ItemImage.objects.filter(file=file_path, item=new_item).exists():
                    new_image = ItemImage(
                        file=File(img_temp, file_path),
                        item=new_item
                    )
                    new_image.save()
                    print(u'Image imported: ', new_image)
                image_count += 1
        if image_count <= 0:
            new_item.status_without_image = True
        new_item.save()
    print(u"%s: imported" % item.id)


def import_items_from_tmp():
    for item in ImportItem.objects.all().prefetch_related('importimage_set'):
        import_item_from_tmp(item)
        item.delete()


def import_some_item_from_tmp():
    try:
        item = ImportItem.objects.all().first()
        import_item_from_tmp(item)
        item.delete()
        return import_some_item_from_tmp()
    except ImportItem.DoesNotExist:
        return 0