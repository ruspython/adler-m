# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table(u'superbanner_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django_resized.forms.ResizedImageField')(max_length=100, max_width=1000, max_height=1000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('color_title', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('color_description', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('button_text', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('button_link', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('color_button', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('color_button_text', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal(u'superbanner', ['Banner'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table(u'superbanner_banner')


    models = {
        u'superbanner.banner': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Banner'},
            'button_link': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'button_text': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'color_button': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'color_button_text': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'color_description': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'color_title': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_resized.forms.ResizedImageField', [], {'max_length': '100', 'max_width': '1000', 'max_height': '1000'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['superbanner']