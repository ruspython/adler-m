# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'KeyWordsExtension'
        db.delete_table(u'adler_keywordsextension')

        # Adding model 'SMSMessage'
        db.create_table(u'adler_smsmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'adler', ['SMSMessage'])


    def backwards(self, orm):
        # Adding model 'KeyWordsExtension'
        db.create_table(u'adler_keywordsextension', (
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('extended_object', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.Page'], unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public_extension', self.gf('django.db.models.fields.related.OneToOneField')(related_name='draft_extension', unique=True, null=True, to=orm['adler.KeyWordsExtension'])),
        ))
        db.send_create_signal(u'adler', ['KeyWordsExtension'])

        # Deleting model 'SMSMessage'
        db.delete_table(u'adler_smsmessage')


    models = {
        u'adler.smsmessage': {
            'Meta': {'object_name': 'SMSMessage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['adler']