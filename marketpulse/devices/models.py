from django.db import models


class Device(models.Model):
    """Model for FfxOS devices data."""

    model = models.CharField(max_length=120, blank=True, default="")
    manufacturer = models.CharField(max_length=120, blank=True, default="")
    is_fxos = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}, {1}'.format(self.manufacturer, self.model)

    class Meta:
        ordering = ['manufacturer', 'model']
        unique_together = ('model', 'manufacturer',)
