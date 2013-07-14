# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'games'
        db.create_table(u'directory_games', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('long', self.gf('django.db.models.fields.FloatField')()),
            ('when', self.gf('django.db.models.fields.DateField')()),
            ('sport', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('isItOpen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('players_needed', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('skill_level', self.gf('django.db.models.fields.CharField')(max_length=11)),
        ))
        db.send_create_signal(u'directory', ['games'])

        # Adding model 'locations'
        db.create_table(u'directory_locations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('when', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'directory', ['locations'])

        # Adding model 'profile'
        db.create_table(u'directory_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('sports_played', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('reputation', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'directory', ['profile'])


    def backwards(self, orm):
        # Deleting model 'games'
        db.delete_table(u'directory_games')

        # Deleting model 'locations'
        db.delete_table(u'directory_locations')

        # Deleting model 'profile'
        db.delete_table(u'directory_profile')


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
            'when': ('django.db.models.fields.DateField', [], {})
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