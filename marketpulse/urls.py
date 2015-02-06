from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Apps
    url(r'', include('marketpulse.base.urls', 'base')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
