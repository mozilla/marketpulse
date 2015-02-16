from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'home.html')


def activities(request):
    return redirect(reverse('main:fxosprice_new'))


def fxosprice_new(request):
    return render(request, 'fxosprice_new.html')
