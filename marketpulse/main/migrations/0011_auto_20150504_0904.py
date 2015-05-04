# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150302_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'ordering': ['-updated_on']},
        ),
    ]
