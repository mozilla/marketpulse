from django.conf import settings
from django.db import models

from uuslug import uuslug

from marketpulse.devices.models import Device
from marketpulse.geo.models import LocationBase


class Activity(models.Model):
    """Model for activity types."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'activity'
        verbose_name_plural = 'activities'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Custom save method."""

        if not self.id:
            self.slug = uuslug(self.name, instance=self)
        super(Activity, self).save(*args, **kwargs)


class Location(LocationBase):
    """Model for contribution location."""

    address = models.CharField(max_length=120, blank=True, default='')
    shop_name = models.CharField(max_length=120)
    link = models.URLField(max_length=500, blank=True, default='')
    is_online = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}, {1}'.format(self.shop_name, self.country)


class Plan(models.Model):
    """Mobile phone plan information."""

    has_plan = models.BooleanField(default=False)
    duration = models.IntegerField(default=None)
    description = models.TextField(default='', blank=True)


class Contribution(models.Model):
    """Model for contribution data."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contributions')
    activity = models.ForeignKey(Activity, related_name='contributions')
    location = models.ForeignKey(Location, related_name='contributions')
    device = models.ForeignKey(Device, related_name='contributions')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, default='')
    availability = models.BooleanField(default=True)
    plan = models.ManyToManyField(Plan, through='Price', null=True, default=None)


class Price(models.Model):
    """Mobile phone price model."""

    contribution = models.ForeignKey(Contribution)
    plan = models.ForeignKey(Plan)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3, choices=[])
