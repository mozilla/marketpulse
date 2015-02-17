from django.contrib import admin

from django_countries import countries
from import_export import fields, resources
from import_export.admin import ExportMixin

from marketpulse.main.models import Activity, Contribution, Location, Plan, Price


class ActivityResource(resources.ModelResource):
    class Meta:
        model = Activity


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location


class ContributionResource(resources.ModelResource):
    country = fields.Field()

    class Meta:
        model = Contribution
        fields = ('user__id', 'user__first_name', 'user__last_name', 'activity__id',
                  'activity__name', 'location__region', 'location__city', 'location__lat',
                  'location__lng', 'device__name', 'device__model', 'device__manufacturer',
                  'created_on', 'updated_on', 'comment', 'availability')

    def dehydrate_country(self, contribution):
        if contribution.location.country:
            return '{0}'.format(dict(countries)[contribution.location.country.code])
        return ''


class PriceResource(resources.ModelResource):
    class Meta:
        model = Price
        fields = ('id', 'contribution__id', 'plan__has_plan', 'plan__duration',
                  'plan__description', 'amount', 'currency')


@admin.register(Activity)
class ActivityAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ActivityResource
    list_display = ('name', 'slug')


@admin.register(Location)
class LocationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LocationResource
    list_display = ('shop_name', 'link', 'address')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('description', 'duration', 'has_plan')


class PriceInline(admin.StackedInline):
    model = Price


@admin.register(Price)
class PriceAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PriceResource
    list_display = ('amount', 'currency')


@admin.register(Contribution)
class ContributionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ContributionResource
    list_display = ('user', 'activity', 'created_on')
    readonly_fields = ('created_on', 'updated_on')
    inlines = [PriceInline]
