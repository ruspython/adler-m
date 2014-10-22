# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EmailTemplate.sender'
        db.alter_column(u'email_templates_emailtemplate', 'sender', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

    def backwards(self, orm):

        # Changing field 'EmailTemplate.sender'
        db.alter_column(u'email_templates_emailtemplate', 'sender', self.gf('django.db.models.fields.EmailField')(default='', max_length=75))

    models = {
        u'email_templates.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'recipients': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'template': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['email_templates']