# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150224_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrier',
            options={'ordering': ['name']},
        ),
    ]
