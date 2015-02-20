# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150220_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='monthly_fee',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plan',
            name='carrier',
            field=models.ForeignKey(related_name='carriers', blank=True, to='main.Carrier', null=True),
            preserve_default=True,
        ),
    ]
