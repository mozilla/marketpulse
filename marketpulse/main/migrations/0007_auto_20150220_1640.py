# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150220_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='amount',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plan',
            name='monthly_fee',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=True,
        ),
    ]
