# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150506_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='slug',
            field=models.SlugField(default=b'', unique=True, max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
