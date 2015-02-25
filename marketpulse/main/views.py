from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse

from marketpulse.geo.lookup import reverse_geocode
from marketpulse.main import FFXOS_ACTIVITY_NAME, forms
from marketpulse.main.models import Activity, Contribution


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:activities'))
    return render(request, 'home.html')


@login_required
def edit_fxosprice(request, username='', id=None):
    user = request.user

    if request.is_ajax():
        country_code = None
        lat = request.GET.get('latitude')
        lng = request.GET.get('longitude')

        if lat and lng:
            location_data = reverse_geocode(lat, lng)
            country_code = location_data.get('country')
        return JsonResponse({'country': country_code})

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
def all_fxosprice(request):
    user = request.user
    contributions = Contribution.objects.filter(user=user.pk)
    return render(request, 'fxosprice_all.html',
                  {'user': user, 'contributions': contributions})


@login_required
def delete_fxosprice(request, contribution_pk):
    user = request.user

    if not Contribution.objects.filter(user=user.pk, pk=contribution_pk).exists():
        raise Http404()

    Contribution.objects.get(user=user.pk, pk=contribution_pk).delete()
    messages.success(request, 'Contribution successfully deleted')
    return redirect(reverse('main:activities'))


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
