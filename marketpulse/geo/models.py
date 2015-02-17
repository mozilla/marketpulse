from django.db import models

from django_countries.fields import CountryField


class LocationBase(models.Model):
    """Model for geolocation data."""

    country = CountryField(blank_label='(Select Country)', null=True, blank=True)
    region = models.CharField(max_length=120, blank=True, default='')
    city = models.CharField(max_length=120, blank=True, default='')
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True
