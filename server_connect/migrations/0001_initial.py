# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConnectSetting'
        db.create_table(u'server_connect_connectsetting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'server_connect', ['ConnectSetting'])


    def backwards(self, orm):
        # Deleting model 'ConnectSetting'
        db.delete_table(u'server_connect_connectsetting')


    models = {
        u'server_connect.connectsetting': {
            'Meta': {'ordering': "['key']", 'object_name': 'ConnectSetting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['server_connect']