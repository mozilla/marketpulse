# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150217_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='country_code',
        ),
        migrations.AddField(
            model_name='location',
            name='is_online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='shop_name',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
