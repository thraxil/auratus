from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=256, default="no title")
    uploaded = models.DateTimeField(auto_now_add=True)
    taken = models.DateTimeField(null=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField(default="", blank=True, null=True)
    description_html = models.TextField(default="", blank=True, null=True)
    views = models.IntegerField(default=0)

    # reticulum fields
    reticulum_key = models.CharField(max_length=256, default="")
    extension = models.CharField(max_length=256, default="jpg")

    class Meta:
        ordering = [
            "-uploaded",
        ]

    def add_tag(self, tag):
        t, created = Tag.objects.get_or_create(name=tag)
        pt, created = PhotoTag.objects.get_or_create(photo=self, tag=t)


class Album(models.Model):
    title = models.CharField(max_length=256, default="no title")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField(default="")
    description_html = models.TextField(default="", blank=True, null=True)

    class Meta:
        ordering = ["-created"]


class AlbumPhoto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = "album"


class Tag(models.Model):
    name = models.CharField(max_length=256, default="")

    class Meta:
        ordering = [
            "name",
        ]


class PhotoTag(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
