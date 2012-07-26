# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table('main_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='no title', max_length=256)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('taken', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reticulum_key', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
            ('extension', self.gf('django.db.models.fields.CharField')(default='jpg', max_length=256)),
        ))
        db.send_create_signal('main', ['Photo'])

        # Adding model 'Album'
        db.create_table('main_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='no title', max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('main', ['Album'])

        # Adding model 'AlbumPhoto'
        db.create_table('main_albumphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Album'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Photo'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('main', ['AlbumPhoto'])

        # Adding model 'Tag'
        db.create_table('main_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
        ))
        db.send_create_signal('main', ['Tag'])

        # Adding model 'PhotoTag'
        db.create_table('main_phototag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Photo'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Tag'])),
        ))
        db.send_create_signal('main', ['PhotoTag'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table('main_photo')

        # Deleting model 'Album'
        db.delete_table('main_album')

        # Deleting model 'AlbumPhoto'
        db.delete_table('main_albumphoto')

        # Deleting model 'Tag'
        db.delete_table('main_tag')

        # Deleting model 'PhotoTag'
        db.delete_table('main_phototag')


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