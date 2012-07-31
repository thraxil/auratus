from django.core.management.base import BaseCommand
from django.utils.simplejson import loads
from auratus.main.models import Photo, Album, Tag, AlbumPhoto
import os
from datetime import datetime
import pytz
import requests

RETICULUM_BASE = "http://behemoth.ccnmtl.columbia.edu:14002/"


class Command(BaseCommand):
    args = 'directory to import from'
    help = 'pull the pagetree data down from production'

    def handle(self, *args, **options):
        # clear everything out to start with
        Tag.objects.all().delete()
        Photo.objects.all().delete()
        Album.objects.all().delete()
        AlbumPhoto.objects.all().delete()

        for directory in args:
            idmap = dict()
            images = set([filename for filename in os.listdir(directory)
                          if filename.endswith("jpg")])
            image_json = [filename for filename in os.listdir(directory)
                          if filename.endswith("json")
                          and not filename.startswith("set_")]
            sets_json = [filename for filename in os.listdir(directory)
                         if filename.endswith("json")
                         and filename.startswith("set_")]
            for filename in image_json:
                print "Image", filename

                # find the matching image and upload it to reticulum
                flickrid = os.path.splitext(filename)[0]
                image_filename = flickrid + ".jpg"
                if image_filename not in images:
                    print "no image found"
                    continue

                fullpath = os.path.join(directory, image_filename)
                files = {'image':
                             (image_filename,
                              open(fullpath, 'rb'))
                         }
                r = requests.post(RETICULUM_BASE, files=files)
                rhash = loads(r.text)["hash"]

                json = loads(open(os.path.join(directory, filename)).read())
                taken = datetime.strptime(json['taken'], "%Y-%m-%d %H:%M:%S")
                p = Photo.objects.create(
                    title=json['title'],
                    description=json['description'],
                    taken=pytz.utc.localize(taken),
                    modified=datetime.utcfromtimestamp(
                        float(int(json['lastupdate']))),
                    uploaded=datetime.utcfromtimestamp(
                        float(int(json['dateuploaded']))),
                    views=int(json['views']),
                    reticulum_key=rhash,
                    extension='jpg',
                    )
                for tag in json['tags']:
                    p.add_tag(tag)
                idmap[flickrid] = p

            for filename in sets_json:
                json = loads(open(os.path.join(directory, filename)).read())
                print "Set", filename
                a = Album.objects.create(
                    title=json['title'],
                    description=json['description'],
                    created=datetime.utcfromtimestamp(
                        float(int(json['date_create']))),
                    modified=datetime.utcfromtimestamp(
                        float(int(json['date_update']))),
                    )
                for flickrid in json['images']:
                    p = idmap[flickrid]
                    AlbumPhoto.objects.get_or_create(album=a, photo=p)
