from django import forms

from models import Device


class DeviceForm(forms.ModelForm):
    """Form for new device input."""

    class Meta:
        model = Device
        fields = ['model', 'manufacturer', 'is_fxos']

    def save(self, *args, **kwargs):
        """Custom save for DeviceForm."""

        # Check if already existing ``similar`` object exists
        query = {
            "model__iexact": self.cleaned_data['model'],
            "manufacturer__iexact": self.cleaned_data['manufacturer']
        }

        qs = Device.objects.filter(**query)
        if qs.exists():
            return qs[0]

        return super(DeviceForm, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """Custom clean for DeviceForm fields."""
        model = self.cleaned_data.get('model')
        manufacturer = self.cleaned_data.get('manufacturer')
        is_fxos = self.cleaned_data.get('is_fxos')
        self.cleaned_data['is_fxos'] = bool(is_fxos)

        # Manually handle required fields to facilitate both fxos/non-fxos devices
        if not is_fxos:
            msg = 'This field is required'
            if not model:
                self._errors['model'] = self.error_class([msg])
            if not manufacturer:
                self._errors['manufacturer'] = self.error_class([msg])

        return self.cleaned_data
