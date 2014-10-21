# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.status_without_image'
        db.add_column(u'catalog_item', 'status_without_image',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Item.status_action'
        db.alter_column(u'catalog_item', 'status_action', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Item.status_sale'
        db.alter_column(u'catalog_item', 'status_sale', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Item.status_new'
        db.alter_column(u'catalog_item', 'status_new', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Item.status_back_in_stock'
        db.alter_column(u'catalog_item', 'status_back_in_stock', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Item.status_on_the_way'
        db.alter_column(u'catalog_item', 'status_on_the_way', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Item.status_not_available'
        db.alter_column(u'catalog_item', 'status_not_available', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'ItemImage.file'
        db.alter_column(u'catalog_itemimage', 'file', self.gf('django_resized.forms.ResizedImageField')(max_length=100, max_width=1020, max_height=1000))

    def backwards(self, orm):
        # Deleting field 'Item.status_without_image'
        db.delete_column(u'catalog_item', 'status_without_image')


        # Changing field 'Item.status_action'
        db.alter_column(u'catalog_item', 'status_action', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.status_sale'
        db.alter_column(u'catalog_item', 'status_sale', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.status_new'
        db.alter_column(u'catalog_item', 'status_new', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.status_back_in_stock'
        db.alter_column(u'catalog_item', 'status_back_in_stock', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.status_on_the_way'
        db.alter_column(u'catalog_item', 'status_on_the_way', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.status_not_available'
        db.alter_column(u'catalog_item', 'status_not_available', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'ItemImage.file'
        db.alter_column(u'catalog_itemimage', 'file', self.gf('django_resized.forms.ResizedImageField')(max_length=100, max_height=1000, max_width=1000))

    models = {
        u'catalog.item': {
            'Meta': {'ordering': "['id']", 'object_name': 'Item'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'brand_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'brand_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'color_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'color_ru': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer_ru': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'new_before': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'series_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'series_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status_action': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_back_in_stock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_not_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_on_the_way': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_without_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.ItemTag']", 'symmetrical': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'catalog.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            'file': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '1020', 'max_height': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Item']"})
        },
        u'catalog.itemtag': {
            'Meta': {'object_name': 'ItemTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'catalog.itemtype': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '200', 'max_height': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['catalog']