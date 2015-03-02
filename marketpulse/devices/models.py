from django.db import models


class Device(models.Model):
    """Model for FfxOS devices data."""

    model = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=120)

    def __unicode__(self):
        return '{0}, {1}'.format(self.manufacturer, self.model)

    class Meta:
        ordering = ['manufacturer', 'model']
