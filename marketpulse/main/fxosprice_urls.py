from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^new/$', 'edit_fxosprice', name='edit_fxosprice'),
    url(r'^contributions/$', 'all_fxosprice', name='all_fxosprice'),
    url(r'^delete/(?P<contribution_pk>\d+)/$', 'delete_fxosprice', name='delete_fxosprice'),
)
