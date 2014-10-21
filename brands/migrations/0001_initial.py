# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table(u'brands_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('image', self.gf('django_resized.forms.ResizedImageField')(max_length=100, max_width=1000, max_height=1000)),
            ('description', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('web_site', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal(u'brands', ['Brand'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table(u'brands_brand')


    models = {
        u'brands.brand': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Brand'},
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '1000', 'max_height': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'web_site': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['brands']