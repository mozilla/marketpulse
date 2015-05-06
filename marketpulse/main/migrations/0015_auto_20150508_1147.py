# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20150508_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='slug',
            field=models.SlugField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
