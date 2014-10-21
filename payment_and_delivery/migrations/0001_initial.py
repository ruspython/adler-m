# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'payment_and_delivery_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal(u'payment_and_delivery', ['Country'])

        # Adding model 'City'
        db.create_table(u'payment_and_delivery_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['payment_and_delivery.Country'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('points', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('courier', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('postal', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'payment_and_delivery', ['City'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'payment_and_delivery_country')

        # Deleting model 'City'
        db.delete_table(u'payment_and_delivery_city')


    models = {
        u'payment_and_delivery.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payment_and_delivery.Country']"}),
            'courier': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'points': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'postal': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'})
        },
        u'payment_and_delivery.country': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        }
    }

    complete_apps = ['payment_and_delivery']