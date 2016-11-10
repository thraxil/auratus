import django.views.static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import TemplateView
from auratus.main.views import (
    index, PhotoView, albums, AlbumView, AddPhoto, AlbumSlideshow, tags,
    tag, AddAlbum, BulkAddPhotos,
)
admin.autodiscover()


urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', view=index, name='index'),
    url(r'smoketest/', include('smoketest.urls')),
    url(r'^page/(?P<page>\d+)/$', view=index, name='page'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
    url(r'^album/$', view=albums, name='album-index'),
    url(r'^album/(?P<pk>\d+)/$', AlbumView.as_view(), name='album'),
    url(r'^album/(?P<id>\d+)/add_photo/$',
        view=login_required(AddPhoto.as_view()),
        name='add-photo'),
    url(r'^album/(?P<id>\d+)/bulk/(?P<token>[^\/]+)/$',
        BulkAddPhotos.as_view(), name='bulk-add'),
    url(r'^album/(?P<pk>\d+)/slideshow/$', AlbumSlideshow.as_view(),
        name='album-slideshow'),
    url(r'^tag/$', view=tags, name='tag-index'),
    url(r'^tag/(?P<tag>\w+)/$', view=tag, name='tag'),
    url(r'^add_album/$', view=login_required(AddAlbum.as_view()),
        name='add-album'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stats/', TemplateView.as_view(template_name="stats.html")),
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
