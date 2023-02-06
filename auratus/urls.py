import django.views.static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, re_path
from django.views.generic import TemplateView

from .main.views import (AddAlbum, AddPhoto, AlbumSlideshow, AlbumsView,
                         AlbumView, BulkAddPhotos, Index, PhotoView, TagsView,
                         TagView)

admin.autodiscover()


urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^$", Index.as_view(), name="index"),
    re_path(r"smoketest/", include("smoketest.urls")),
    re_path(r"^page/(?P<page>\d+)/$", Index.as_view(), name="page"),
    re_path(r"^photo/(?P<pk>\d+)/$", PhotoView.as_view(), name="photo"),
    re_path(r"^album/$", AlbumsView.as_view(), name="album-index"),
    re_path(r"^album/(?P<pk>\d+)/$", AlbumView.as_view(), name="album"),
    re_path(
        r"^album/(?P<id>\d+)/add_photo/$",
        view=login_required(AddPhoto.as_view()),
        name="add-photo",
    ),
    re_path(
        r"^album/(?P<id>\d+)/bulk/(?P<token>[^\/]+)/$",
        BulkAddPhotos.as_view(),
        name="bulk-add",
    ),
    re_path(
        r"^album/(?P<pk>\d+)/slideshow/$",
        AlbumSlideshow.as_view(),
        name="album-slideshow",
    ),
    re_path(r"^tag/$", TagsView.as_view(), name="tag-index"),
    re_path(r"^tag/(?P<slug>\w+)/$", TagView.as_view(), name="tag"),
    re_path(
        r"^add_album/$",
        view=login_required(AddAlbum.as_view()),
        name="add-album",
    ),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^stats/", TemplateView.as_view(template_name="stats.html")),
    re_path(
        r"^uploads/(?P<path>.*)$",
        django.views.static.serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ]
