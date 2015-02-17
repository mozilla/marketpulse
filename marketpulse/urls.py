from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

import jingo.monkey


jingo.monkey.patch()


urlpatterns = patterns(
    '',
    # Apps
    url(r'', include('{0}.main.urls'.format(settings.PROJECT_MODULE), namespace='main')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
