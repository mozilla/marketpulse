from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from django_countries import countries
from django_countries.fields import CountryField
from uuslug import uuslug

from marketpulse.devices.models import Device
from marketpulse.geo.models import LocationBase
from marketpulse.main import get_currency_choices


class Activity(models.Model):
    """Model for activity types."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'activity'
        verbose_name_plural = 'activities'

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        """Custom save method."""

        if not self.id:
            self.slug = uuslug(self.name, instance=self)
        super(Activity, self).save(*args, **kwargs)


class Location(LocationBase):
    """Model for contribution location."""

    address = models.CharField(max_length=120, blank=True, default='')
    shop_name = models.CharField(max_length=120, blank=True, default='Media upload')
    link = models.URLField(max_length=500, blank=True, default='')
    is_online = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}, {1}'.format(self.shop_name, self.country)


class Contribution(models.Model):
    """Model for contribution data."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contributions')
    activity = models.ForeignKey(Activity, related_name='contributions')
    location = models.ForeignKey(Location, related_name='contributions', null=True)
    device = models.ForeignKey(Device, related_name='contributions', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, default='')
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='ffos', blank=True)

    class Meta:
        ordering = ['-updated_on']

    def __unicode__(self):
        return u'{0}, {1}'.format(self.user, self.activity)


class Carrier(models.Model):
    name = models.CharField(max_length=128)
    parent_operator = models.CharField(max_length=128, blank=True, default='')
    country = CountryField(null=True, blank=True)

    def __unicode__(self):
        all_countries = dict(countries)
        country = self.country
        if self.country.code in all_countries:
            country = all_countries[self.country.code]

        return u'{0}, {1}, {2}'.format(self.name, country, self.parent_operator)

    class Meta:
        ordering = ['name']


class Plan(models.Model):
    """Mobile phone plan information."""

    contribution = models.ForeignKey(Contribution, related_name='plans', null=True)
    has_plan = models.BooleanField(default=False)
    duration = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(default='', blank=True)
    amount = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])
    currency = models.CharField(max_length=128, choices=get_currency_choices(), default='')
    carrier = models.ForeignKey(Carrier, related_name='carriers', null=True, blank=True)
    monthly_fee = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0)])


class Vote(models.Model):
    """Vote model.

    Register the upvotes/confirmations for each contribution.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='voted_on')
    contribution = models.ForeignKey(Contribution, related_name='votes')
    date_voted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'contribution',)

    def __unicode__(self):
        return u'{0}, {1}'.format(self.user, self.contribution)
