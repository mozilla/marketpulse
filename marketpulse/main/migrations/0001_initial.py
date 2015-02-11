# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(default=b'', blank=True)),
                ('availability', models.BooleanField(default=True)),
                ('activity', models.ForeignKey(related_name='contributions', to='main.Activity')),
                ('device', models.ForeignKey(related_name='contributions', to='devices.Device')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(unique=True, max_length=120)),
                ('country_code', models.CharField(max_length=2)),
                ('region', models.CharField(default=b'', max_length=120, blank=True)),
                ('city', models.CharField(max_length=120)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
                ('address', models.CharField(max_length=120)),
                ('shop_name', models.CharField(default=b'', max_length=120, blank=True)),
                ('link', models.URLField(default=b'', max_length=500, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('has_plan', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=None)),
                ('description', models.TextField(default=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
                ('contribution', models.ForeignKey(to='main.Contribution')),
                ('plan', models.ForeignKey(to='main.Plan')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contribution',
            name='location',
            field=models.ForeignKey(related_name='contributions', to='main.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='plan',
            field=models.ManyToManyField(default=None, to='main.Plan', null=True, through='main.Price'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contribution',
            name='user',
            field=models.ForeignKey(related_name='contributions', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
