# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'games.when'
        db.alter_column(u'directory_games', 'when', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'games.when'
        db.alter_column(u'directory_games', 'when', self.gf('django.db.models.fields.DateField')())

    models = {
        u'directory.games': {
            'Meta': {'object_name': 'games'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isItOpen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'long': ('django.db.models.fields.FloatField', [], {}),
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
            'sports_played': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['directory']