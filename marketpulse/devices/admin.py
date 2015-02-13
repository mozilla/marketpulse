from django.contrib import admin

from marketpulse.devices.models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'manufacturer')

admin.site.register(Device, DeviceAdmin)
