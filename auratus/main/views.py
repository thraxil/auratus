from annoying.decorators import render_to
from auratus.main.models import Photo, Album, Tag, AlbumPhoto
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from json import loads
import os
import requests


@render_to('main/index.html')
def index(request, page=1):
    photo_list = Photo.objects.all()
    p = Paginator(photo_list, 50)
    try:
        photos = p.page(page)
    except PageNotAnInteger:
        photos = p.page(1)
    except EmptyPage:
        photos = p.page(p.num_pages)
    return dict(photos=photos.object_list,
                paginator=photos)


@render_to('main/albums.html')
def albums(request):
    return dict(albums=Album.objects.all())


@render_to('main/tags.html')
def tags(request):
    return dict(tags=Tag.objects.all())


@render_to('main/photo.html')
def photo(request, id):
    p = get_object_or_404(Photo, pk=id)
    return dict(photo=p)


@render_to('main/album.html')
def album(request, id):
    a = get_object_or_404(Album, pk=id)
    return dict(album=a)


@login_required
@render_to('main/add_album.html')
def add_album(request):
    if request.method == 'POST':
        a = Album.objects.create(
            title=request.POST.get('title', 'no title'),
            description=request.POST.get('description', ''))
        return HttpResponseRedirect(reverse('album', args=(a.id,)))
    return dict()


def add_photo(request, id):
    a = get_object_or_404(Album, pk=id)
    if request.FILES.get('image', None):
        original_filename = request.FILES['image'].name
        extension = os.path.splitext(original_filename)[1].lower()
        print original_filename
        if extension == ".jpeg":
            extension = ".jpg"
        if extension not in [".jpg", ".png", ".gif"]:
            return HttpResponse("unsupported image format")
        title = request.POST.get('title', original_filename)
        files = {
            'image': ("image%s" % extension, request.FILES['image'])
        }
        r = requests.post("http://reticulum.thraxil.org/", files=files)
        p = Photo.objects.create(
            title=title,
            reticulum_key=loads(r.text)["hash"],
            extension=extension,
            description=request.POST.get('description', ''))
        AlbumPhoto.objects.create(
            album=a,
            photo=p)
        return HttpResponseRedirect(reverse('album', args=(a.id,)))
    else:
        return HttpResponse("no image")


@render_to('main/album_slideshow.html')
def album_slideshow(request, id):
    a = get_object_or_404(Album, pk=id)
    return dict(album=a)


@render_to('main/tag.html')
def tag(request, tag):
    t = get_object_or_404(Tag, name=tag)
    return dict(tag=t)
