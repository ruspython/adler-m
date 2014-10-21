# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.client_name'
        db.add_column(u'order_order', 'client_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.client_second_name'
        db.add_column(u'order_order', 'client_second_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.client_last_name'
        db.add_column(u'order_order', 'client_last_name',
                      self.gf('django.db.models.fields.CharField')(default=22, max_length=32),
                      keep_default=False)

        # Adding field 'Order.address_city'
        db.add_column(u'order_order', 'address_city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.address_house'
        db.add_column(u'order_order', 'address_house',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.address_building'
        db.add_column(u'order_order', 'address_building',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.address_flat'
        db.add_column(u'order_order', 'address_flat',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.address_zipcode'
        db.add_column(u'order_order', 'address_zipcode',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)

        # Adding field 'Order.phone'
        db.add_column(u'order_order', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.client_name'
        db.delete_column(u'order_order', 'client_name')

        # Deleting field 'Order.client_second_name'
        db.delete_column(u'order_order', 'client_second_name')

        # Deleting field 'Order.client_last_name'
        db.delete_column(u'order_order', 'client_last_name')

        # Deleting field 'Order.address_city'
        db.delete_column(u'order_order', 'address_city')

        # Deleting field 'Order.address_house'
        db.delete_column(u'order_order', 'address_house')

        # Deleting field 'Order.address_building'
        db.delete_column(u'order_order', 'address_building')

        # Deleting field 'Order.address_flat'
        db.delete_column(u'order_order', 'address_flat')

        # Deleting field 'Order.address_zipcode'
        db.delete_column(u'order_order', 'address_zipcode')

        # Deleting field 'Order.phone'
        db.delete_column(u'order_order', 'phone')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'order.order': {
            'Meta': {'ordering': "['-add_time']", 'object_name': 'Order'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'address_building': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'address_flat': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'address_house': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'address_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_second_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'total_price': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['order']