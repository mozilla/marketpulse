# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20150302_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_fxos',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='manufacturer',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('model', 'manufacturer')]),
        ),
    ]
