from django.conf import settings
from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^$', 'home', name='home'),
    url(r'^fxosprice/', include('{0}.main.fxosprice_urls'.format(settings.PROJECT_MODULE))),
)
