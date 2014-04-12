# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainBlock'
        db.create_table('web_mainblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('page_section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.PageSection'])),
        ))
        db.send_create_signal('web', ['MainBlock'])

        # Adding model 'Main'
        db.create_table('web_main', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('moderate_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.ModerateState'])),
            ('date_moderated', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('user_moderated', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('edit_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['block.EditState'])),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content', to=orm['web.MainBlock'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True, null=True)),
        ))
        db.send_create_signal('web', ['Main'])

        # Adding unique constraint on 'Main', fields ['block', 'moderate_state']
        db.create_unique('web_main', ['block_id', 'moderate_state_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Main', fields ['block', 'moderate_state']
        db.delete_unique('web_main', ['block_id', 'moderate_state_id'])

        # Deleting model 'MainBlock'
        db.delete_table('web_mainblock')

        # Deleting model 'Main'
        db.delete_table('web_main')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'block.editstate': {
            'Meta': {'object_name': 'EditState', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'block.moderatestate': {
            'Meta': {'object_name': 'ModerateState', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'block.page': {
            'Meta': {'object_name': 'Page', 'unique_together': "(('slug', 'slug_menu'),)", 'ordering': "['order', 'slug', 'slug_menu']"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_menu': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'block.pagesection': {
            'Meta': {'object_name': 'PageSection', 'unique_together': "(('page', 'section'),)", 'ordering': "('page__slug', 'section__slug')"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Page']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.Section']"})
        },
        'block.section': {
            'Meta': {'object_name': 'Section', 'ordering': "('name',)"},
            'block_app': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'block_model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'create_url_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web.main': {
            'Meta': {'object_name': 'Main', 'unique_together': "(('block', 'moderate_state'),)"},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content'", 'to': "orm['web.MainBlock']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'date_moderated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'edit_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.EditState']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderate_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.ModerateState']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'user_moderated': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'web.mainblock': {
            'Meta': {'object_name': 'MainBlock'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'page_section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['block.PageSection']"})
        }
    }

    complete_apps = ['web']