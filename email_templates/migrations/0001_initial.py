# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailTemplate'
        db.create_table(u'email_templates_emailtemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=128)),
            ('recipients', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('template', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'email_templates', ['EmailTemplate'])


    def backwards(self, orm):
        # Deleting model 'EmailTemplate'
        db.delete_table(u'email_templates_emailtemplate')


    models = {
        u'email_templates.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'recipients': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'template': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['email_templates']