# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogUploadedModel'
        db.create_table(u'blog_bloguploadedmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('brand_ru', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('brand_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('type_ru', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('type_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note_ru', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('series_ru', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('series_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('scale', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('manufacturer_ru', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('manufacturer_en', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('color_ru', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('color_en', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['BlogUploadedModel'])

        # Adding field 'Blog.title_ru'
        db.add_column(u'blog_blog', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=1280, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blog.title_en'
        db.add_column(u'blog_blog', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1280, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blog.announce_ru'
        db.add_column(u'blog_blog', 'announce_ru',
                      self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blog.announce_en'
        db.add_column(u'blog_blog', 'announce_en',
                      self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blog.text_ru'
        db.add_column(u'blog_blog', 'text_ru',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Blog.text_en'
        db.add_column(u'blog_blog', 'text_en',
                      self.gf('ckeditor.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field uploaded_item on 'Blog'
        m2m_table_name = db.shorten_name(u'blog_blog_uploaded_item')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm[u'blog.blog'], null=False)),
            ('bloguploadedmodel', models.ForeignKey(orm[u'blog.bloguploadedmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blog_id', 'bloguploadedmodel_id'])


    def backwards(self, orm):
        # Deleting model 'BlogUploadedModel'
        db.delete_table(u'blog_bloguploadedmodel')

        # Deleting field 'Blog.title_ru'
        db.delete_column(u'blog_blog', 'title_ru')

        # Deleting field 'Blog.title_en'
        db.delete_column(u'blog_blog', 'title_en')

        # Deleting field 'Blog.announce_ru'
        db.delete_column(u'blog_blog', 'announce_ru')

        # Deleting field 'Blog.announce_en'
        db.delete_column(u'blog_blog', 'announce_en')

        # Deleting field 'Blog.text_ru'
        db.delete_column(u'blog_blog', 'text_ru')

        # Deleting field 'Blog.text_en'
        db.delete_column(u'blog_blog', 'text_en')

        # Removing M2M table for field uploaded_item on 'Blog'
        db.delete_table(db.shorten_name(u'blog_blog_uploaded_item'))


    models = {
        u'blog.blog': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Blog'},
            'announce': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'announce_en': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'announce_ru': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 9, 18, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['catalog.Item']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.BlogTag']", 'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1280'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '1280', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '1280', 'null': 'True', 'blank': 'True'}),
            'uploaded_item': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'uploaded'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['blog.BlogUploadedModel']"})
        },
        u'blog.blogtag': {
            'Meta': {'object_name': 'BlogTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'blog.bloguploadedmodel': {
            'Meta': {'object_name': 'BlogUploadedModel'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'brand_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'brand_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'color_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'color_ru': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer_ru': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'series_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'series_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'catalog.item': {
            'Meta': {'ordering': "['id']", 'object_name': 'Item'},
            'article': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'brand_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'brand_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'color_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'color_ru': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manufacturer_ru': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'new_before': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'default': "'model'", 'max_length': '16'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'series_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'series_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status_action': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_back_in_stock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_not_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_on_the_way': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_without_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['catalog.ItemTag']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'type_ru': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'catalog.itemtag': {
            'Meta': {'object_name': 'ItemTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['blog']