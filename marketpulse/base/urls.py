from django.conf.urls import patterns, url


urlpatterns = patterns(
    'marketpulse.base.views',
    url(r'^$', 'home', name='home'),
)
