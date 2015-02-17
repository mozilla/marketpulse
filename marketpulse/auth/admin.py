from django.contrib import admin
from django.contrib.auth.models import User

from import_export import resources
from import_export.admin import ExportMixin


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    class Meta:
        model = User


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
