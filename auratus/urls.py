from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
import os.path
admin.autodiscover()
import staticmedia

site_media_root = os.path.join(os.path.dirname(__file__), "../media")

redirect_after_logout = getattr(settings, 'LOGOUT_REDIRECT_URL', None)
auth_urls = (r'^accounts/',
             include('django.contrib.auth.urls'))
logout_page = (r'^accounts/logout/$',
               'django.contrib.auth.views.logout',
               {'next_page': redirect_after_logout})
if hasattr(settings, 'WIND_BASE'):
    auth_urls = (r'^accounts/',
                 include('djangowind.urls'))
    logout_page = (r'^accounts/logout/$',
                   'djangowind.views.logout',
                   {'next_page': redirect_after_logout})

urlpatterns = patterns('',
                       auth_urls,
                       logout_page,
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
                       url(r'^album/(?P<id>\d+)/slideshow/$',
                           view='auratus.main.views.album_slideshow',
                           name='album-slideshow'),
                       url(r'^tag/$',
                           view='auratus.main.views.tags',
                           name='tag-index'),
                       url(r'^tag/(?P<tag>\w+)/$',
                           view='auratus.main.views.tag',
                           name='tag'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^stats/', direct_to_template,
                        {'template': 'stats.html'}),
                       (r'^site_media/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': site_media_root}),
                       (r'^uploads/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
) + staticmedia.serve()
