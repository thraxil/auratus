import django.views.static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import TemplateView
from .main.views import (
    Index, PhotoView, AlbumsView, AlbumView, AddPhoto, AlbumSlideshow,
    TagsView, TagView, AddAlbum, BulkAddPhotos,
)
admin.autodiscover()


urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'smoketest/', include('smoketest.urls')),
    url(r'^page/(?P<page>\d+)/$', Index.as_view(), name='page'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
    url(r'^album/$', AlbumsView.as_view(), name='album-index'),
    url(r'^album/(?P<pk>\d+)/$', AlbumView.as_view(), name='album'),
    url(r'^album/(?P<id>\d+)/add_photo/$',
        view=login_required(AddPhoto.as_view()),
        name='add-photo'),
    url(r'^album/(?P<id>\d+)/bulk/(?P<token>[^\/]+)/$',
        BulkAddPhotos.as_view(), name='bulk-add'),
    url(r'^album/(?P<pk>\d+)/slideshow/$', AlbumSlideshow.as_view(),
        name='album-slideshow'),
    url(r'^tag/$', TagsView.as_view(), name='tag-index'),
    url(r'^tag/(?P<slug>\w+)/$', TagView.as_view(), name='tag'),
    url(r'^add_album/$', view=login_required(AddAlbum.as_view()),
        name='add-album'),
    url(r'^admin/', admin.site.urls),
    url(r'^stats/', TemplateView.as_view(template_name="stats.html")),
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
