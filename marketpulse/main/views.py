from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def activities(request):
    return redirect(reverse('main:fxosprice_new'))


def fxosprice_new(request):
    return render(request, 'fxosprice_new.html',
                  {'mapbox_id': settings.MAPBOX_MAP_ID, 'mapbox_token': settings.MAPBOX_TOKEN})
