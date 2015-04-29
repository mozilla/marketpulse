from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse

import moneyed
from django_countries import countries

from marketpulse.geo.lookup import reverse_geocode
from marketpulse.main import FFXOS_ACTIVITY_NAME, forms
from marketpulse.main.models import Activity, Contribution
from marketpulse.devices.models import Device


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:activities'))
    return render(request, 'home.html')


@login_required
def edit_fxosprice(request, username='', id=None):
    user = request.user

    if request.is_ajax():
        lat = request.GET.get('latitude')
        lng = request.GET.get('longitude')

        data = {'country': None,
                'currency': None}

        location_data = reverse_geocode(lat, lng)
        country_code = location_data.get('country')
        if country_code:
            data['country'] = country_code
            country_name = dict(countries)[country_code]

            for currency, currency_data in moneyed.CURRENCIES.items():
                if country_name.upper() in currency_data.countries:
                    data['currency'] = currency
                    break

        return JsonResponse(data)

    if not id:
        activity = Activity.objects.get(name=FFXOS_ACTIVITY_NAME)
        contribution = Contribution(activity=activity, user=user)
    else:
        contribution = get_object_or_404(Contribution, pk=id, user=user)

    contribution_form = forms.ContributionForm(request.POST or None, instance=contribution)
    location_form = forms.LocationForm(request.POST or None)
    plan_formset = forms.PlanFormset(request.POST or None, instance=contribution)

    if location_form.is_valid() and contribution_form.is_valid() and plan_formset.is_valid():
        location = location_form.save()
        obj = contribution_form.save(commit=False)
        obj.location = location
        obj.save()
        plan_formset.save()

        messages.success(request, 'Contribution successfully saved')
        contribution_form = forms.ContributionForm()
        location_form = forms.LocationForm()
        plan_formset = forms.PlanFormset()

        return redirect(reverse('main:activities'))

    return render(request, 'fxosprice_new.html',
                  {'contribution_form': contribution_form,
                   'location_form': location_form,
                   'plan_formset': plan_formset,
                   'mapbox_id': settings.MAPBOX_MAP_ID,
                   'mapbox_token': settings.MAPBOX_TOKEN})


@login_required
def all_fxosprice(request, user_pk=None):
    user = request.user
    contributions = Contribution.objects.all()
    if user_pk:
        contributions = Contribution.objects.filter(user=user_pk)

    devices = Device.objects.all()
    all_countries = []
    for code, name in list(countries):
        all_countries.append({'code': code, 'name': name})

    country_code = request.GET.get('country_code')
    device_pk = request.GET.get('device_pk')
    if country_code:
        contributions = contributions.filter(location__country=country_code)
    if device_pk:
        contributions = contributions.filter(device=device_pk)
        device_pk = int(device_pk)

    return render(request, 'fxosprice_all.html',
                  {'user': user, 'contributions': contributions,
                  'devices': devices,
                  'countries': all_countries,
                  'country_code': country_code,
                  'device_pk': device_pk})


@login_required
def view_fxosprice(request, contribution_pk):
    user = request.user
    contribution = get_object_or_404(Contribution, pk=contribution_pk)
    return render(request, 'fxosprice_view.html',
                  {'user': user, 'contribution': contribution,
                   'mapbox_id': settings.MAPBOX_MAP_ID,
                   'mapbox_token': settings.MAPBOX_TOKEN})


@login_required
def delete_fxosprice(request, contribution_pk):
    user = request.user

    if not Contribution.objects.filter(user=user.pk, pk=contribution_pk).exists():
        raise Http404()

    Contribution.objects.get(user=user.pk, pk=contribution_pk).delete()
    messages.success(request, 'Contribution successfully deleted')
    return redirect(reverse('main:all_fxosprice'))


@login_required
def activities(request):
    user = request.user
    user_contributions = Contribution.objects.filter(user=user.pk).count()
    total_contributions = Contribution.objects.all().count()
    try:
        percent = int((float(user_contributions) / float(total_contributions)) * 100)
    except ZeroDivisionError:
        percent = 0
    return render(request, 'activities.html',
                  {'user': request.user,
                   'user_contributions': user_contributions,
                   'percent': percent})


def manifest(request):
    data = render(request, 'manifest.webapp')
    response = HttpResponse(data,
                            content_type='application/x-web-app-manifest+json; charset=utf-8')
    response['Content-Disposition'] = 'attachment;filename=manifest.webapp'
    return response
