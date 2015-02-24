# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from django_countries import countries

CARRIERS = {
    'Telefonica Digital': [{'Movistar': ['Spain', 'Colombia', 'Venezuela', 'Peru',
                                         'Uruguay', 'Mexico', 'Chile', 'El Salvador',
                                         'Nicaragua', 'Guatemala', 'Costa Rica']},
                           {'Vivo': ['Brazil']},
                           {'O2': ['Germany']}],
    'Deutsche Telekom': [{'T-Mobile': ['Poland', 'Czech Republic', 'Macedonia']},
                         {'Congstar': ['Germany']},
                         {'Telekom': ['Hungary']},
                         {'Cosmote': ['Greece']}],
    'Telenor': [{'Telenor': ['Hugnary', 'Serbia', 'Montenegro']},
                {'Grameenphone': ['Bangladesh']}],
    'Telecom Italia': [{'TIM': ['Italy']}],
    'America Movil': [{'Telcel': ['Mexico']}],
    'Retailer': [{'E.Leclerc': ['France']}],
    'Snapdeal': [{'Spice': ['India']}],
    'JB Hifi': [{'ZTE': ['Australia']}],
    'Alcatel OneTouch': [{'TCL': ['India']}],
    'www.flicpart.com': [{'ZEN Mobil': ['India']}],
    'Megafon': [{'Megafon': ['Russia']}],
    'Cherry Mobile': [{'Cherry Mobile': ['Philippines']}],
    'Banglalink': [{'Banglalink': ['Bangladesh']}],
    'KDDI': [{'KDDI': ['Japan']}]
}


COUNTRIES_DICT = {v: k for k, v in countries}


def remove_carriers(apps, schema_editor):
    Carrier = apps.get_model('main', 'Carrier')
    Carrier.objects.all().delete()


def add_carriers(apps, schema_editor):

    Carrier = apps.get_model('main', 'Carrier')
    for parent_operator, carriers in CARRIERS.items():
        for carrier_data in carriers:
            for carrier, carrier_countries in carrier_data.items():
                for carrier_country in carrier_countries:
                    if carrier_country in COUNTRIES_DICT:
                        Carrier.objects.create(parent_operator=parent_operator,
                                               name=carrier,
                                               country=COUNTRIES_DICT[carrier_country])
                        continue
    Carrier.objects.create(parent_operator='Other', name='Other')


def backwards_method(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150220_1830'),
    ]

    operations = [
        migrations.RunPython(remove_carriers, backwards_method),
        migrations.RunPython(add_carriers, remove_carriers),
    ]
