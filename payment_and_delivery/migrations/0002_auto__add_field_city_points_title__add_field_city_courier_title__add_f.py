# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'City.points_title'
        db.add_column(u'payment_and_delivery_city', 'points_title',
                      self.gf('django.db.models.fields.CharField')(max_length=1128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'City.courier_title'
        db.add_column(u'payment_and_delivery_city', 'courier_title',
                      self.gf('django.db.models.fields.CharField')(max_length=1128, null=True, blank=True),
                      keep_default=False)

        # Adding field 'City.postal_title'
        db.add_column(u'payment_and_delivery_city', 'postal_title',
                      self.gf('django.db.models.fields.CharField')(max_length=1128, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'City.points_title'
        db.delete_column(u'payment_and_delivery_city', 'points_title')

        # Deleting field 'City.courier_title'
        db.delete_column(u'payment_and_delivery_city', 'courier_title')

        # Deleting field 'City.postal_title'
        db.delete_column(u'payment_and_delivery_city', 'postal_title')


    models = {
        u'payment_and_delivery.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payment_and_delivery.Country']"}),
            'courier': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'courier_title': ('django.db.models.fields.CharField', [], {'max_length': '1128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'points': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'points_title': ('django.db.models.fields.CharField', [], {'max_length': '1128', 'null': 'True', 'blank': 'True'}),
            'postal': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'postal_title': ('django.db.models.fields.CharField', [], {'max_length': '1128', 'null': 'True', 'blank': 'True'})
        },
        u'payment_and_delivery.country': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        }
    }

    complete_apps = ['payment_and_delivery']