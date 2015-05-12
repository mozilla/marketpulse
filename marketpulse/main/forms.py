from urlparse import urlparse

from django import forms
from django.forms.models import BaseInlineFormSet

from marketpulse.devices.models import Device
from marketpulse.geo.lookup import reverse_geocode
from marketpulse.main.models import Contribution, Location


class ContributionForm(forms.ModelForm):

    class Meta:
        model = Contribution
        fields = ['device', 'comment', 'availability']
        widgets = {'availability': forms.CheckboxInput()}

    def __init__(self, *args, **kwargs):
        """Dynamically initialize Contribution form."""
        self.clone = kwargs.pop('clone', False)
        self.is_fxos = kwargs.pop('is_fxos', True)

        super(ContributionForm, self).__init__(*args, **kwargs)

        if not self.is_fxos:
            self.fields['device'].required = False
        self.fields['device'].queryset = Device.objects.filter(is_fxos=True)

    def save(self, *args, **kwargs):
        """Override save method to handle contribution cloning."""
        if self.clone:
            # Force a new entry in the db
            self.instance.pk = None
        return super(ContributionForm, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """Custom clean for ContributionForm fields."""
        cleaned_data = super(ContributionForm, self).clean(*args, **kwargs)

        # When a non-fxos device is selected nullify fxos dropdown
        if not self.is_fxos:
            cleaned_data['device'] = None

        return cleaned_data


class ImageForm(forms.ModelForm):

    class Meta:
        model = Contribution
        fields = ['image', 'comment']


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['shop_name', 'lat', 'lng', 'link', 'country', 'is_online']
        widgets = {'lat': forms.HiddenInput(),
                   'lng': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        """Dynamically initialize Location form."""
        self.is_media = kwargs.pop('is_media', False)
        super(LocationForm, self).__init__(*args, **kwargs)
        if not self.is_media:
            self.fields['shop_name'].initial = 'Please add the name of the shop'

    def clean(self):
        cdata = super(LocationForm, self).clean()
        url = cdata.get('link')
        if cdata['is_online']:
            if not cdata['country']:
                msg = 'Please provide a country'
                self._errors['country'] = self.error_class([msg])
            if not url:
                msg = 'Please provide a URL'
                self._errors['link'] = self.error_class([msg])

        if url and not urlparse(url).scheme:
            url = 'http://' + url
            cdata['link'] = url

        return cdata

    def save(self, commit=True):
        instance = super(LocationForm, self).save(commit=False)
        location_data = reverse_geocode(instance.lat, instance.lng)

        for attr in ['country', 'region', 'city', 'address']:
            setattr(instance, attr, location_data.get(attr, ''))

        if commit:
            instance.save()

        return instance


class BasePlanFormset(BaseInlineFormSet):

    def clean(self):
        """Clean formset."""

        if any(self.errors):
            return

        for i, form in enumerate(self.forms):
            has_plan = form.cleaned_data.get('has_plan')
            amount = form.cleaned_data.get('amount')
            duration = form.cleaned_data.get('duration')
            carrier = form.cleaned_data.get('carrier')
            monthly_fee = form.cleaned_data.get('monthly_fee')

            if has_plan:
                if not duration:
                    msg = 'Please provide the duration of this plan'
                    self._errors[i]['duration'] = self.error_class([msg])
                if not carrier:
                    msg = 'Please provide the carrier for this plan'
                    self._errors[i]['carrier'] = self.error_class([msg])
                if not monthly_fee:
                    msg = 'Please enter the monthly fee for this plan'
                    self._errors[i]['monthly_fee'] = self.error_class([msg])
            if not has_plan and not amount:
                msg = 'Please enter the price of this device'
                self._errors[i]['amount'] = self.error_class([msg])
