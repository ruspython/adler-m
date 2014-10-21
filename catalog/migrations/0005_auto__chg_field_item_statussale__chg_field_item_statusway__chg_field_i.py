# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.statussale'
        db.alter_column(u'catalog_item', 'statussale', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.statusway'
        db.alter_column(u'catalog_item', 'statusway', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.statusaction'
        db.alter_column(u'catalog_item', 'statusaction', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.statusnotavail'
        db.alter_column(u'catalog_item', 'statusnotavail', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.statusnew'
        db.alter_column(u'catalog_item', 'statusnew', self.gf('django.db.models.fields.BooleanField')(max_length=256))

        # Changing field 'Item.statusnewavail'
        db.alter_column(u'catalog_item', 'statusnewavail', self.gf('django.db.models.fields.BooleanField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'Item.statussale'
        db.alter_column(u'catalog_item', 'statussale', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Item.statusway'
        db.alter_column(u'catalog_item', 'statusway', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Item.statusaction'
        db.alter_column(u'catalog_item', 'statusaction', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Item.statusnotavail'
        db.alter_column(u'catalog_item', 'statusnotavail', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Item.statusnew'
        db.alter_column(u'catalog_item', 'statusnew', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Item.statusnewavail'
        db.alter_column(u'catalog_item', 'statusnewavail', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

    models = {
        u'catalog.item': {
            'Meta': {'ordering': "['id']", 'object_name': 'Item'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'newbefore': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pricemin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'statusaction': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'statusnew': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'statusnewavail': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'statusnotavail': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'statussale': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'statusway': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.ItemTag']", 'symmetrical': 'False'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'catalog.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            'file': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '1000', 'max_height': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Item']"})
        },
        u'catalog.itemtag': {
            'Meta': {'object_name': 'ItemTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['catalog']