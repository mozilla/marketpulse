import json

from django.contrib import admin

from django_countries import countries
from import_export import fields, resources
from import_export.admin import ExportMixin

from marketpulse.main.models import Activity, Carrier, Contribution, Location, Plan, Vote


class ActivityResource(resources.ModelResource):

    class Meta:
        model = Activity


class LocationResource(resources.ModelResource):

    class Meta:
        model = Location


class ContributionResource(resources.ModelResource):
    country = fields.Field()
    plans = fields.Field()

    class Meta:
        model = Contribution
        fields = ('id', 'user__id', 'user__first_name', 'user__last_name', 'user__email',
                  'activity__id', 'activity__name', 'location__region', 'location__city',
                  'location__lat', 'location__lng', 'device__model', 'device__manufacturer',
                  'created_on', 'updated_on', 'comment', 'availability')

    def dehydrate_country(self, contribution):
        if contribution.location.country:
            return '{0}'.format(dict(countries)[contribution.location.country.code])
        return ''

    def dehydrate_plans(self, contribution):
        qs = contribution.plans.all()
        if qs.exists():
            plans = qs.values('has_plan', 'duration', 'description', 'amount', 'currency',
                              'carrier__name', 'carrier__name', 'carrier__parent_operator',
                              'carrier__country')
            return json.dumps(list(plans), indent=4)
        else:
            return ''


class PlanResource(resources.ModelResource):
    has_plan = fields.Field()

    class Meta:
        model = Plan
        fields = ('contribution__id', 'duration', 'description', 'amount',
                  'currency', 'carrier__name', 'carrier__parent_operator', 'carrier__country',
                  'monthly_fee')

    def dehydrate_has_plan(self, plan):
        return str(plan.has_plan)


@admin.register(Activity)
class ActivityAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ActivityResource
    list_display = ('name', 'slug')


@admin.register(Location)
class LocationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LocationResource
    list_display = ('shop_name', 'link', 'address')


@admin.register(Carrier)
class CarrierAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'parent_operator', 'country')


@admin.register(Plan)
class PlanAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PlanResource
    list_display = ('contribution', 'amount', 'has_plan', 'duration')


@admin.register(Contribution)
class ContributionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ContributionResource
    list_display = ('user', 'activity', 'created_on')
    readonly_fields = ('created_on', 'updated_on')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'contribution', 'date_voted',)
