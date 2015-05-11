# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mozillians_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mozillians_username',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
