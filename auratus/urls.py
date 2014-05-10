from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
admin.autodiscover()


urlpatterns = patterns(
    '',
    (r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$',
        view='auratus.main.views.index',
        name='index'),
    url(r'^page/(?P<page>\d+)/$',
        view='auratus.main.views.index',
        name='page'),
    url(r'^photo/(?P<id>\d+)/$',
        view='auratus.main.views.photo',
        name='photo'),
    url(r'^album/$',
        view='auratus.main.views.albums',
        name='album-index'),
    url(r'^album/(?P<id>\d+)/$',
        view='auratus.main.views.album',
        name='album'),
    url(r'^album/(?P<id>\d+)/add_photo/$',
        view='auratus.main.views.add_photo',
        name='add-photo'),
    url(r'^album/(?P<id>\d+)/slideshow/$',
        view='auratus.main.views.album_slideshow',
        name='album-slideshow'),
    url(r'^tag/$',
        view='auratus.main.views.tags',
        name='tag-index'),
    url(r'^tag/(?P<tag>\w+)/$',
        view='auratus.main.views.tag',
        name='tag'),
    url(r'^add_album/$',
        view='auratus.main.views.add_album',
        name='add-album'),
    (r'^admin/', include(admin.site.urls)),
    (r'^stats/', TemplateView.as_view(template_name="stats.html")),
    (r'^uploads/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
