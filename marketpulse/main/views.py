from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.http import Http404

from marketpulse.main import FFXOS_ACTIVITY_NAME, forms
from marketpulse.main.models import Activity, Contribution


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('main:activities'))
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

        return redirect(reverse('main:activities'))

    return render(request, 'fxosprice_new.html',
                  {'contribution_form': contribution_form,
                   'location_form': location_form,
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
                   'total_contributions': total_contributions,
                   'percent': percent})
