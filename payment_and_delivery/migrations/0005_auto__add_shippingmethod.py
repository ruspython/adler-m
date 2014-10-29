# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShippingMethod'
        db.create_table(u'payment_and_delivery_shippingmethod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shipping_types', self.gf('django.db.models.fields.CharField')(default='post', max_length=32, blank=True)),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'payment_and_delivery', ['ShippingMethod'])


    def backwards(self, orm):
        # Deleting model 'ShippingMethod'
        db.delete_table(u'payment_and_delivery_shippingmethod')


    models = {
        u'payment_and_delivery.city': {
            'Meta': {'ordering': "['country', 'name']", 'object_name': 'City'},
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
        },
        u'payment_and_delivery.pointaddress': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'PointAddress'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payment_and_delivery.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('addresspicker.fields.AddressPickerField', [], {'default': '\'{"latlng":"0,0","zoom":5}\'', 'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        u'payment_and_delivery.shippingmethod': {
            'Meta': {'object_name': 'ShippingMethod'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'shipping_types': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '32', 'blank': 'True'})
        }
    }

    complete_apps = ['payment_and_delivery']