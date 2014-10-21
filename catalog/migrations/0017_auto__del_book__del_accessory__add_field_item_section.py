# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'catalog_book')

        # Removing M2M table for field tags on 'Book'
        db.delete_table(db.shorten_name(u'catalog_book_tags'))

        # Deleting model 'Accessory'
        db.delete_table(u'catalog_accessory')

        # Removing M2M table for field tags on 'Accessory'
        db.delete_table(db.shorten_name(u'catalog_accessory_tags'))

        # Adding field 'Item.section'
        db.add_column(u'catalog_item', 'section',
                      self.gf('django.db.models.fields.CharField')(default='model', max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'catalog_book', (
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['Book'])

        # Adding M2M table for field tags on 'Book'
        m2m_table_name = db.shorten_name(u'catalog_book_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'catalog.book'], null=False)),
            ('itemtag', models.ForeignKey(orm[u'catalog.itemtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'itemtag_id'])

        # Adding model 'Accessory'
        db.create_table(u'catalog_accessory', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            ('scale', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('price_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['Accessory'])

        # Adding M2M table for field tags on 'Accessory'
        m2m_table_name = db.shorten_name(u'catalog_accessory_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accessory', models.ForeignKey(orm[u'catalog.accessory'], null=False)),
            ('itemtag', models.ForeignKey(orm[u'catalog.itemtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['accessory_id', 'itemtag_id'])

        # Deleting field 'Item.section'
        db.delete_column(u'catalog_item', 'section')


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