# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PublicFile'
        db.create_table(u'public_files_publicfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('content_type', self.gf('django.db.models.fields.CharField')(default='text/plain', max_length=128)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'public_files', ['PublicFile'])


    def backwards(self, orm):
        # Deleting model 'PublicFile'
        db.delete_table(u'public_files_publicfile')


    models = {
        u'public_files.publicfile': {
            'Meta': {'ordering': "['path']", 'object_name': 'PublicFile'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'text/plain'", 'max_length': '128'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['public_files']