from django.db import models


class LocationBase(models.Model):
    """Model for geolocation data."""

    country = models.CharField(max_length=120, unique=True)
    country_code = models.CharField(max_length=2)
    region = models.CharField(max_length=120, blank=True, default='')
    city = models.CharField(max_length=120)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True
