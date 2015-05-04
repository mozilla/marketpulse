from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse

import moneyed
from django_countries import countries

from marketpulse.geo.lookup import reverse_geocode
from marketpulse.main import FFXOS_ACTIVITY_NAME, forms
from marketpulse.main.models import Activity, Contribution, Plan
from marketpulse.devices.models import Device


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:activities'))
    return render(request, 'home.html')


@login_required
def edit_contribution(request, contribution_pk=None):
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

    if not contribution_pk:
        activity = Activity.objects.get(name=FFXOS_ACTIVITY_NAME)
        contribution = Contribution(activity=activity, user=user)
        location = None
        extra = 1
    else:
        contribution = get_object_or_404(Contribution, pk=contribution_pk, user=user)
        location = contribution.location
        extra = 0

    contribution_form = forms.ContributionForm(request.POST or None, instance=contribution)

    location_form = forms.LocationForm(request.POST or None, instance=location)
    PlanFormset = inlineformset_factory(Contribution, Plan, formset=forms.BasePlanFormset,
                                        extra=extra, can_delete=False)
    plan_formset = PlanFormset(request.POST or None, instance=contribution)

    if location_form.is_valid() and contribution_form.is_valid() and plan_formset.is_valid():
        location = location_form.save()
        obj = contribution_form.save(commit=False)
        obj.location = location
        obj.save()
        plan_formset.save()

        messages.success(request, 'Contribution successfully saved')
        contribution_form = forms.ContributionForm()
        location_form = forms.LocationForm()
        plan_formset = PlanFormset()

        return redirect(reverse('main:list_my_contributions'))

    return render(request, 'fxosprice_new.html',
                  {'contribution_form': contribution_form,
                   'location_form': location_form,
                   'plan_formset': plan_formset,
                   'mapbox_id': settings.MAPBOX_MAP_ID,
                   'mapbox_token': settings.MAPBOX_TOKEN})


@login_required
def list_my_contributions(request):
    """View contributions of logged-in user."""

    return list_contributions(request, user=request.user)


@login_required
def list_contributions(request, user=None):
    """View to list either all the contributions
    or the contributions of a user.

    """

    contributions = Contribution.objects.all()
    if user:
        contributions = Contribution.objects.filter(user=user)

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
                  {'contributions': contributions,
                   'devices': devices,
                   'countries': all_countries,
                   'country_code': country_code,
                   'device_pk': device_pk})


@login_required
def view_contribution(request, contribution_pk):
    user = request.user
    contribution = get_object_or_404(Contribution, pk=contribution_pk)
    return render(request, 'fxosprice_view.html',
                  {'user': user, 'contribution': contribution,
                   'mapbox_id': settings.MAPBOX_MAP_ID,
                   'mapbox_token': settings.MAPBOX_TOKEN})


@login_required
def delete_contribution(request, contribution_pk):
    user = request.user

    if not Contribution.objects.filter(user=user.pk, pk=contribution_pk).exists():
        raise Http404()

    Contribution.objects.get(user=user.pk, pk=contribution_pk).delete()
    messages.success(request, 'Contribution successfully deleted')
    return redirect(reverse('main:list_contributions'))


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
