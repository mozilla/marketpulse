from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^new/$', 'edit_fxosprice', name='edit_fxosprice'),
    url(r'^contributions/all/$', 'list_contributions', name='list_contributions'),
    url(r'^contributions/me/$', 'list_my_contributions', name='list_my_contributions'),
    url(r'^contribution/(?P<contribution_pk>\d+)/$', 'view_fxosprice', name='view_fxosprice'),
    url(r'^delete/(?P<contribution_pk>\d+)/$', 'delete_fxosprice', name='delete_fxosprice'),
)
