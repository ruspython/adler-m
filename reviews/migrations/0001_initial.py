# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'reviews_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('add_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('review', self.gf('django.db.models.fields.TextField')()),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal(u'reviews', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'reviews_review')


    models = {
        u'reviews.review': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Review'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'review': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['reviews']