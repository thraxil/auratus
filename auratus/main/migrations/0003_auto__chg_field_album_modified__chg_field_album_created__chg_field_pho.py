# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Album.modified'
        db.alter_column('main_album', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Album.created'
        db.alter_column('main_album', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Photo.uploaded'
        db.alter_column('main_photo', 'uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Photo.modified'
        db.alter_column('main_photo', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):

        # Changing field 'Album.modified'
        db.alter_column('main_album', 'modified', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Album.created'
        db.alter_column('main_album', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Photo.uploaded'
        db.alter_column('main_photo', 'uploaded', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Photo.modified'
        db.alter_column('main_photo', 'modified', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'main.album': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Album'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'no title'", 'max_length': '256'})
        },
        'main.albumphoto': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AlbumPhoto'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Photo']"})
        },
        'main.photo': {
            'Meta': {'ordering': "['-uploaded']", 'object_name': 'Photo'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "'jpg'", 'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'reticulum_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'no title'", 'max_length': '256'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'main.phototag': {
            'Meta': {'object_name': 'PhotoTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Photo']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Tag']"})
        },
        'main.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'})
        }
    }

    complete_apps = ['main']
