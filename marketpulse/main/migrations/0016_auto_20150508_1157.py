# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from marketpulse.main import FFXOS_MEDIA_ACTIVITY_NAME


def new_activity(apps, schema_editor):
    Activity = apps.get_model("main", "Activity")
    Activity.objects.create(name=FFXOS_MEDIA_ACTIVITY_NAME)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150508_1147'),
    ]

    operations = [
        migrations.RunPython(new_activity),
    ]
