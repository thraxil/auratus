from annoying.decorators import render_to
from auratus.main.models import Photo, Album, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


@render_to('main/album_slideshow.html')
def album_slideshow(request, id):
    a = get_object_or_404(Album, pk=id)
    return dict(album=a)


@render_to('main/tag.html')
def tag(request, tag):
    t = get_object_or_404(Tag, name=tag)
    return dict(tag=t)
