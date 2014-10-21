# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Faq'
        db.create_table(u'faq_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal(u'faq', ['Faq'])


    def backwards(self, orm):
        # Deleting model 'Faq'
        db.delete_table(u'faq_faq')


    models = {
        u'faq.faq': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Faq'},
            'answer': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'question': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['faq']