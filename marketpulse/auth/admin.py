from django.contrib import admin
from django.contrib.auth import get_user_model

from import_export import resources
from import_export.admin import ExportMixin


User = get_user_model()


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'mozillians_url')


class UserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ['username', 'email', 'first_name', 'last_name']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
