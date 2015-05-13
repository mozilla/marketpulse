from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


import jingo.monkey


jingo.monkey.patch()


urlpatterns = patterns(
    '',

    # Apps
    url(r'', include('{0}.auth.urls'.format(settings.PROJECT_MODULE))),
    url(r'', include('{0}.main.urls'.format(settings.PROJECT_MODULE), namespace='main')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

# In DEBUG mode, serve static/media files through Django
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
