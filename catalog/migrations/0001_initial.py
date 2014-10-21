# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'catalog_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('scale', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('pricemin', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('newbefore', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('statusnew', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('statusnotavail', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('statusnewavail', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('statusaction', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('statussale', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('statusway', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['Item'])

        # Adding model 'ItemImage'
        db.create_table(u'catalog_itemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django_resized.forms.ResizedImageField')(max_length=100, max_width=1000, max_height=1000)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Item'])),
        ))
        db.send_create_signal(u'catalog', ['ItemImage'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'catalog_item')

        # Deleting model 'ItemImage'
        db.delete_table(u'catalog_itemimage')


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
            'price': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'pricemin': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'statusaction': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'statusnew': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'statusnewavail': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'statusnotavail': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'statussale': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'statusway': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'catalog.itemimage': {
            'Meta': {'object_name': 'ItemImage'},
            'file': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '1000', 'max_height': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Item']"})
        }
    }

    complete_apps = ['catalog']