from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^contributions/all/$', 'list_contributions', name='list_contributions'),
    url(r'^contributions/me/$', 'list_my_contributions', name='list_my_contributions'),
    url(r'^contribution/(?P<contribution_pk>\d+)/$', 'view_contribution',
        name='view_contribution'),
    url(r'^new/$', 'edit_contribution', name='new_contribution'),
    url(r'^contribution/(?P<contribution_pk>\d+)/edit/$', 'edit_contribution',
        name='edit_contribution'),
    url(r'^contribution/(?P<contribution_pk>\d+)/delete/$', 'delete_contribution',
        name='delete_contribution'),
)
