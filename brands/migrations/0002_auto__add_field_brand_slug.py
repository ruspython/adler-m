# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Brand.slug'
        db.add_column(u'brands_brand', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Brand.slug'
        db.delete_column(u'brands_brand', 'slug')


    models = {
        u'brands.brand': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Brand'},
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '1000', 'max_height': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'web_site': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['brands']