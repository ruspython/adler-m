# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PointAddress.address'
        db.alter_column(u'payment_and_delivery_pointaddress', 'address', self.gf('django.db.models.fields.TextField')(max_length=512))

    def backwards(self, orm):

        # Changing field 'PointAddress.address'
        db.alter_column(u'payment_and_delivery_pointaddress', 'address', self.gf('django.db.models.fields.CharField')(max_length=512))

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
            'map': ('addresspicker.fields.AddressPickerField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['payment_and_delivery']