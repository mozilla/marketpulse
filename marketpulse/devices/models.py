from django.db import models


class Device(models.Model):
    """Model for FfxOS devices data."""

    name = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=120, unique=True)

    def __unicode__(self):
        return self.name
