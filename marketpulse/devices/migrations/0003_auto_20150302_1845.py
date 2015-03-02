# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20150220_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['manufacturer', 'model']},
        ),
    ]
