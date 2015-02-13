from django.contrib import admin

from marketpulse.main.models import Activity, Contribution, Location, Plan, Price


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    list_display = ('name', 'slug')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('address', 'shop_name', 'link')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    model = Plan
    list_display = ('description', 'duration', 'has_plan')


class PriceInline(admin.StackedInline):
    model = Price


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'created_on')
    readonly_fields = ('created_on', 'updated_on')
    inlines = [PriceInline]
