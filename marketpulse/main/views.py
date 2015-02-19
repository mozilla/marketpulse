from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse

from marketpulse.main import FFXOS_ACTIVITY_NAME, forms
from marketpulse.main.models import Activity, Contribution


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:edit_fxosprice'))
    return render(request, 'home.html')


@login_required
def edit_fxosprice(request, username='', id=None):
    user = request.user

    if not id:
        activity = Activity.objects.get(name=FFXOS_ACTIVITY_NAME)
        contribution = Contribution(activity=activity, user=user)
    else:
        contribution = get_object_or_404(Contribution, pk=id, user=user)

    contribution_form = forms.ContributionForm(request.POST or None, instance=contribution)
    location_form = forms.LocationForm(request.POST or None)

    if location_form.is_valid() and contribution_form.is_valid():
        location = location_form.save()
        obj = contribution_form.save(commit=False)
        obj.location = location
        obj.save()

        messages.success(request, 'Contribution successfully saved')

    return render(request, 'fxosprice_new.html',
                  {'contribution_form': contribution_form,
                   'location_form': location_form,
                   'mapbox_id': settings.MAPBOX_MAP_ID,
                   'mapbox_token': settings.MAPBOX_TOKEN})


def fxosprice_home(request):
    return render(request, 'home.html')
