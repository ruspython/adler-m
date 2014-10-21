# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Item.statussale'
        db.delete_column(u'catalog_item', 'statussale')

        # Deleting field 'Item.statusway'
        db.delete_column(u'catalog_item', 'statusway')

        # Deleting field 'Item.statusaction'
        db.delete_column(u'catalog_item', 'statusaction')

        # Deleting field 'Item.pricemin'
        db.delete_column(u'catalog_item', 'pricemin')

        # Deleting field 'Item.statusnotavail'
        db.delete_column(u'catalog_item', 'statusnotavail')

        # Deleting field 'Item.statusnew'
        db.delete_column(u'catalog_item', 'statusnew')

        # Deleting field 'Item.statusnewavail'
        db.delete_column(u'catalog_item', 'statusnewavail')

        # Deleting field 'Item.newbefore'
        db.delete_column(u'catalog_item', 'newbefore')

        # Adding field 'Item.price_min'
        db.add_column(u'catalog_item', 'price_min',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.new_before'
        db.add_column(u'catalog_item', 'new_before',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.status_new'
        db.add_column(u'catalog_item', 'status_new',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.status_not_available'
        db.add_column(u'catalog_item', 'status_not_available',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.status_back_in_stock'
        db.add_column(u'catalog_item', 'status_back_in_stock',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.status_action'
        db.add_column(u'catalog_item', 'status_action',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.status_sale'
        db.add_column(u'catalog_item', 'status_sale',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.status_on_the_way'
        db.add_column(u'catalog_item', 'status_on_the_way',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Item.statussale'
        db.add_column(u'catalog_item', 'statussale',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.statusway'
        db.add_column(u'catalog_item', 'statusway',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.statusaction'
        db.add_column(u'catalog_item', 'statusaction',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.pricemin'
        db.add_column(u'catalog_item', 'pricemin',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.statusnotavail'
        db.add_column(u'catalog_item', 'statusnotavail',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.statusnew'
        db.add_column(u'catalog_item', 'statusnew',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.statusnewavail'
        db.add_column(u'catalog_item', 'statusnewavail',
                      self.gf('django.db.models.fields.BooleanField')(default=False, max_length=256),
                      keep_default=False)

        # Adding field 'Item.newbefore'
        db.add_column(u'catalog_item', 'newbefore',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Item.price_min'
        db.delete_column(u'catalog_item', 'price_min')

        # Deleting field 'Item.new_before'
        db.delete_column(u'catalog_item', 'new_before')

        # Deleting field 'Item.status_new'
        db.delete_column(u'catalog_item', 'status_new')

        # Deleting field 'Item.status_not_available'
        db.delete_column(u'catalog_item', 'status_not_available')

        # Deleting field 'Item.status_back_in_stock'
        db.delete_column(u'catalog_item', 'status_back_in_stock')

        # Deleting field 'Item.status_action'
        db.delete_column(u'catalog_item', 'status_action')

        # Deleting field 'Item.status_sale'
        db.delete_column(u'catalog_item', 'status_sale')

        # Deleting field 'Item.status_on_the_way'
        db.delete_column(u'catalog_item', 'status_on_the_way')


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
            'new_before': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status_action': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'status_back_in_stock': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'status_new': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'status_not_available': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'status_on_the_way': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
            'status_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'max_length': '256'}),
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