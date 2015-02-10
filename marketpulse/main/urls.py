from django.conf import settings
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^$', 'home', name='home'),
)
