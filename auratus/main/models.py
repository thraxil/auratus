from django.db import models
from datetime import datetime

class Photo(models.Model):
    title = models.CharField(max_length=256, default="no title")
    uploaded = models.DateTimeField(auto_now_add=False, default=datetime.now)
    taken = models.DateTimeField(null=True)
    modified = models.DateTimeField(auto_now=False, default=datetime.now)
    description = models.TextField(default="", blank=True, null=True)
    views = models.IntegerField(default=0)

    # reticulum fields
    reticulum_key = models.CharField(max_length=256, default="")
    extension = models.CharField(max_length=256, default="jpg")

    class Meta:
        ordering = ['-uploaded',]

class Album(models.Model):
    title = models.CharField(max_length=256, default="no title")
    created = models.DateTimeField(auto_now_add=False, default=datetime.now)
    modified = models.DateTimeField(auto_now=False, default=datetime.now)
    description = models.TextField(default="")

    class Meta:
        ordering = ['-created']

class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album)
    photo = models.ForeignKey(Photo)

    class Meta:
        order_with_respect_to = 'album'

class Tag(models.Model):
    name = models.CharField(max_length=256, default="")
    
class PhotoTag(models.Model):
    photo = models.ForeignKey(Photo)
    tag = models.ForeignKey(Tag)
