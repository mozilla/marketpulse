# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_activity(apps, schema_editor):
    name = 'Submit FirefoxOS device price'
    Activity = apps.get_model('main', 'Activity')
    Activity.objects.create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150217_1001'),
    ]

    operations = [
        migrations.RunPython(add_activity),
    ]
