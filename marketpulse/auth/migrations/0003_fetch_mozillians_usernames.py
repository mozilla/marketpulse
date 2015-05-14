# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

from marketpulse.base.mozillians import MozilliansClient


def fetch_usernames(apps, schema_editor):
    User = apps.get_model("mozillians_auth", "User")
    api_url = settings.MOZILLIANS_API_URL
    api_key = settings.MOZILLIANS_API_KEY
    mozillians_client = MozilliansClient(api_url, api_key)
    for user in User.objects.all():
        try:
            mozillian = mozillians_client.lookup_user({'email': user.email}, detailed=False)
            user.mozillians_username = mozillian['username']
            user.save()
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('mozillians_auth', '0002_user_mozillians_username'),
    ]

    operations = [
        migrations.RunPython(fetch_usernames),
    ]
