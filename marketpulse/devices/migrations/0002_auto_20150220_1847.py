# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.AlterField(
            model_name='device',
            name='manufacturer',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
