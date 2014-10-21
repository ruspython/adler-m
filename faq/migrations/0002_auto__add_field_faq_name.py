# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Faq.name'
        db.add_column(u'faq_faq', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Faq.name'
        db.delete_column(u'faq_faq', 'name')


    models = {
        u'faq.faq': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Faq'},
            'answer': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'question': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['faq']