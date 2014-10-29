# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field shipping_method on 'City'
        m2m_table_name = db.shorten_name(u'payment_and_delivery_city_shipping_method')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('city', models.ForeignKey(orm[u'payment_and_delivery.city'], null=False)),
            ('shippingmethod', models.ForeignKey(orm[u'payment_and_delivery.shippingmethod'], null=False))
        ))
        db.create_unique(m2m_table_name, ['city_id', 'shippingmethod_id'])


    def backwards(self, orm):
        # Removing M2M table for field shipping_method on 'City'
        db.delete_table(db.shorten_name(u'payment_and_delivery_city_shipping_method'))


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
            'postal_title': ('django.db.models.fields.CharField', [], {'max_length': '1128', 'null': 'True', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['payment_and_delivery.ShippingMethod']", 'symmetrical': 'False'})
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
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'shipping_types': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '32', 'blank': 'True'})
        }
    }

    complete_apps = ['payment_and_delivery']