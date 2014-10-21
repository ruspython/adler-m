# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ImportItem.note_en'
        db.alter_column(u'catalog_importitem', 'note_en', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ImportItem.note'
        db.alter_column(u'catalog_importitem', 'note', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'ImportItem.note_en'
        db.alter_column(u'catalog_importitem', 'note_en', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'ImportItem.note'
        db.alter_column(u'catalog_importitem', 'note', self.gf('django.db.models.fields.CharField')(max_length=512))

    models = {
        u'catalog.importitem': {
            'Meta': {'object_name': 'ImportItem'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'author_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'brand_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'color_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'manufacturer_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'note_en': ('django.db.models.fields.TextField', [], {}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'pricemin': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'publisher_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'quantity': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'series_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statusaccess': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statusaction': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statusbook': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statusnew': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statusnewavail': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statuspreorder': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statussale': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'statusway': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tags_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'catalog.item': {
            'Meta': {'ordering': "['id']", 'object_name': 'Item'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
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
            'is_just_updated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'section': ('django.db.models.fields.CharField', [], {'default': "'model'", 'max_length': '16'}),
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['catalog.ItemTag']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'catalog.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['catalog']