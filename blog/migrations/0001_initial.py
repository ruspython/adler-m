# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table(u'blog_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 10, 0, 0), null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1280)),
            ('text', self.gf('ckeditor.fields.RichTextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Blog'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table(u'blog_blog')


    models = {
        u'blog.blog': {
            'Meta': {'ordering': "['date']", 'object_name': 'Blog'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 10, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1280'})
        }
    }

    complete_apps = ['blog']