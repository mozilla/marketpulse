from django.conf import settings
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^$', 'home', name='home'),
    url(r'^activities/$', 'activities', name='activities'),
    url(r'^fxos_price/new/$', 'fxos_price_new', name='fxos_price_new'),
)
