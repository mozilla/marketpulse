from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'home.html')


def activities(request):
    return redirect(reverse('main:fxos_price_new'))


def fxos_price_new(request):
    return render(request, 'fxos_price_new.html')
