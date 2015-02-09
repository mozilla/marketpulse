from django.conf import settings
from django.conf.urls import patterns, url


urlpatterns = patterns(
    url(r'^$', '{0}.views.main'.format(settings.PROJECT_NAME), name='main'),
)
