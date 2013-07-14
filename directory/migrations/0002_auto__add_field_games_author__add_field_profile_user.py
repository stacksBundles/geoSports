# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'games.author'
        db.add_column(u'directory_games', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'profile.user'
        db.add_column(u'directory_profile', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'games.author'
        db.delete_column(u'directory_games', 'author_id')

        # Deleting field 'profile.user'
        db.delete_column(u'directory_profile', 'user_id')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'directory.games': {
            'Meta': {'object_name': 'games'},
            'address': ('django.db.models.fields.CharField', [], {'default': "'default for testing, will be updated later'", 'max_length': '140'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isItOpen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'long': ('django.db.models.fields.FloatField', [], {}),
            'note': ('django.db.models.fields.CharField', [], {'default': "'default for testing, will be updated later'", 'max_length': '140', 'blank': 'True'}),
            'players_needed': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'skill_level': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'when': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'directory.locations': {
            'Meta': {'object_name': 'locations'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'when': ('django.db.models.fields.DateField', [], {})
        },
        u'directory.profile': {
            'Meta': {'object_name': 'profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'reputation': ('django.db.models.fields.IntegerField', [], {}),
            'sports_played': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['directory']