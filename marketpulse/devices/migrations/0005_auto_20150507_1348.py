# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_default_is_fxos_flag(apps, schema_editor):
    """Flag all current devices as fxOS"""
    Device = apps.get_model("devices", "Device")
    Device.objects.all().update(is_fxos=True)


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_auto_20150507_1011'),
    ]

    operations = [
        migrations.RunPython(add_default_is_fxos_flag)
    ]
