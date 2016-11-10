from auratus.main.models import Photo, Album, Tag, AlbumPhoto
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from django.views.generic.detail import DetailView
from itsdangerous import URLSafeSerializer
import os


def index(request, page=1):
    photo_list = Photo.objects.all()
    p = Paginator(photo_list, 50)
    try:
        photos = p.page(page)
    except PageNotAnInteger:
        photos = p.page(1)
    except EmptyPage:
        photos = p.page(p.num_pages)
    return render(
        request,
        'main/index.html',
        dict(photos=photos.object_list,
             paginator=photos))


def albums(request):
    return render(request, 'main/albums.html',
                  dict(albums=Album.objects.all()))


def tags(request):
    return render(request, 'main/tags.html',
                  dict(tags=Tag.objects.all()))


class PhotoView(DetailView):
    template_name = 'main/photo.html'
    model = Photo
    context_object_name = 'photo'


class AlbumView(DetailView):
    template_name = 'main/album.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        serializer = URLSafeSerializer(settings.SECRET_KEY)
        token = serializer.dumps({'album_id': self.object.id})
        context['token'] = token
        context['album'] = self.object
        return context


class AddAlbum(View):
    template_filename = 'main/add_album.html'

    def post(self, request):
        a = Album.objects.create(
            title=request.POST.get('title', 'no title'),
            description=request.POST.get('description', ''))
        return HttpResponseRedirect(reverse('album', args=(a.id,)))

    def get(self, request):
        return render(request, self.template_filename, dict())


class AddPhoto(View):
    def post(self, request, id):
        a = get_object_or_404(Album, pk=id)
        if request.FILES.get('image', None):
            original_filename = request.FILES['image'].name
            extension = os.path.splitext(original_filename)[1].lower()
            if extension == ".jpeg":
                extension = ".jpg"
            if extension not in [".jpg", ".png", ".gif"]:
                return HttpResponse("unsupported image format")
            title = request.POST.get('title', original_filename)
            rhash = settings.UPLOADER.upload(request.FILES['image'])
            p = Photo.objects.create(
                title=title,
                reticulum_key=rhash,
                extension=extension,
                description=request.POST.get('description', ''))
            AlbumPhoto.objects.create(
                album=a,
                photo=p)
            return HttpResponseRedirect(reverse('album', args=(a.id,)))
        else:
            return HttpResponse("no image")


class BulkAddPhotos(View):
    def post(self, request, id, token):
        a = get_object_or_404(Album, pk=id)
        s = URLSafeSerializer(settings.SECRET_KEY)
        d = s.loads(token)
        if d['album_id'] != id:
            return HttpResponse("bad token")

        if request.FILES.get('image', None):
            original_filename = request.FILES['image'].name
            extension = os.path.splitext(original_filename)[1].lower()
            if extension == ".jpeg":
                extension = ".jpg"
            if extension not in [".jpg", ".png", ".gif"]:
                return HttpResponse("unsupported image format")
            title = original_filename
            rhash = settings.UPLOADER.upload(request.FILES['image'])
            p = Photo.objects.create(
                title=title,
                reticulum_key=rhash,
                extension=extension,
                description='')
            AlbumPhoto.objects.create(
                album=a,
                photo=p)
            return HttpResponse("ok")
        else:
            return HttpResponse("no image")


class AlbumSlideshow(DetailView):
    model = Album
    template_name = 'main/album_slideshow.html'
    context_object_name = 'album'


class TagView(DetailView):
    model = Tag
    template_name = 'main/tag.html'
    context_object_name = 'tag'

    def get_object(self):
        return Tag.objects.get(name=self.kwargs['slug'])
