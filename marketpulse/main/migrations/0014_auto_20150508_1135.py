# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150508_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='image',
            field=models.ImageField(upload_to=b'ffos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='shop_name',
            field=models.CharField(default=b'Media upload', max_length=120, blank=True),
            preserve_default=True,
        ),
    ]
