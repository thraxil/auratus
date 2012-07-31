from annoying.decorators import render_to
from auratus.main.models import Photo, Album, Tag
from django.shortcuts import get_object_or_404

@render_to('main/index.html')
def index(request):
    return dict(photos=Photo.objects.all()[:50])


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
