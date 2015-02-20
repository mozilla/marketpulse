# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150218_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('parent_operator', models.CharField(default=b'', max_length=128, blank=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='price',
            name='contribution',
        ),
        migrations.RemoveField(
            model_name='price',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='contribution',
            name='plan',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='plan',
            name='amount',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='carrier',
            field=models.ForeignKey(related_name='carriers', to='main.Carrier', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='contribution',
            field=models.ForeignKey(related_name='plans', to='main.Contribution', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='currency',
            field=models.CharField(default=b'', max_length=128, choices=[('AED', 'UAE Dirham'), ('AFN', 'Afghani'), ('ALL', 'Lek'), ('AMD', 'Armenian Dram'), ('ANG', 'Netherlands Antillian Guilder'), ('AOA', 'Kwanza'), ('ARS', 'Argentine Peso'), ('AUD', 'Australian Dollar'), ('AWG', 'Aruban Guilder'), ('AZN', 'Azerbaijanian Manat'), ('BAM', 'Convertible Marks'), ('BBD', 'Barbados Dollar'), ('BDT', 'Taka'), ('BGN', 'Bulgarian Lev'), ('BHD', 'Bahraini Dinar'), ('BIF', 'Burundi Franc'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('BND', 'Brunei Dollar'), ('BRL', 'Brazilian Real'), ('BSD', 'Bahamian Dollar'), ('BTN', 'Bhutanese ngultrum'), ('BWP', 'Pula'), ('BYR', 'Belarussian Ruble'), ('BZD', 'Belize Dollar'), ('CAD', 'Canadian Dollar'), ('CDF', 'Congolese franc'), ('CHF', 'Swiss Franc'), ('CLP', 'Chilean peso'), ('CNY', 'Yuan Renminbi'), ('COP', 'Colombian peso'), ('CRC', 'Costa Rican Colon'), ('CUC', 'Cuban convertible peso'), ('CUP', 'Cuban Peso'), ('CVE', 'Cape Verde Escudo'), ('CZK', 'Czech Koruna'), ('DJF', 'Djibouti Franc'), ('DKK', 'Danish Krone'), ('DOP', 'Dominican Peso'), ('DZD', 'Algerian Dinar'), ('EEK', 'Kroon'), ('EGP', 'Egyptian Pound'), ('ERN', 'Nakfa'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('FJD', 'Fiji Dollar'), ('FKP', 'Falkland Islands Pound'), ('GBP', 'Pound Sterling'), ('GEL', 'Lari'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('GMD', 'Dalasi'), ('GNF', 'Guinea Franc'), ('GTQ', 'Quetzal'), ('GYD', 'Guyana Dollar'), ('HKD', 'Hong Kong Dollar'), ('HNL', 'Lempira'), ('HRK', 'Croatian Kuna'), ('HTG', 'Haitian gourde'), ('HUF', 'Forint'), ('IDR', 'Rupiah'), ('ILS', 'New Israeli Sheqel'), ('IMP', 'Isle of Man pount'), ('INR', 'Indian Rupee'), ('IQD', 'Iraqi Dinar'), ('IRR', 'Iranian Rial'), ('ISK', 'Iceland Krona'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('JPY', 'Yen'), ('KES', 'Kenyan Shilling'), ('KGS', 'Som'), ('KHR', 'Riel'), ('KMF', 'Comoro Franc'), ('KPW', 'North Korean Won'), ('KRW', 'Won'), ('KWD', 'Kuwaiti Dinar'), ('KYD', 'Cayman Islands Dollar'), ('KZT', 'Tenge'), ('LAK', 'Kip'), ('LBP', 'Lebanese Pound'), ('LKR', 'Sri Lanka Rupee'), ('LRD', 'Liberian Dollar'), ('LSL', 'Lesotho loti'), ('LTL', 'Lithuanian Litas'), ('LVL', 'Latvian Lats'), ('LYD', 'Libyan Dinar'), ('MAD', 'Moroccan Dirham'), ('MDL', 'Moldovan Leu'), ('MGA', 'Malagasy Ariary'), ('MKD', 'Denar'), ('MMK', 'Kyat'), ('MNT', 'Tugrik'), ('MOP', 'Pataca'), ('MRO', 'Ouguiya'), ('MUR', 'Mauritius Rupee'), ('MVR', 'Rufiyaa'), ('MWK', 'Kwacha'), ('MXN', 'Mexixan peso'), ('MYR', 'Malaysian Ringgit'), ('MZN', 'Metical'), ('NAD', 'Namibian Dollar'), ('NGN', 'Naira'), ('NIO', 'Cordoba Oro'), ('NOK', 'Norwegian Krone'), ('NPR', 'Nepalese Rupee'), ('NZD', 'New Zealand Dollar'), ('OMR', 'Rial Omani'), ('PEN', 'Nuevo Sol'), ('PGK', 'Kina'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistan Rupee'), ('PLN', 'Zloty'), ('PYG', 'Guarani'), ('QAR', 'Qatari Rial'), ('RON', 'New Leu'), ('RSD', 'Serbian Dinar'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('SAR', 'Saudi Riyal'), ('SBD', 'Solomon Islands Dollar'), ('SCR', 'Seychelles Rupee'), ('SDG', 'Sudanese Pound'), ('SEK', 'Swedish Krona'), ('SGD', 'Singapore Dollar'), ('SHP', 'Saint Helena Pound'), ('SKK', 'Slovak Koruna'), ('SLL', 'Leone'), ('SOS', 'Somali Shilling'), ('SRD', 'Surinam Dollar'), ('STD', 'Dobra'), ('SYP', 'Syrian Pound'), ('SZL', 'Lilangeni'), ('THB', 'Baht'), ('TJS', 'Somoni'), ('TMM', 'Manat'), ('TND', 'Tunisian Dinar'), ('TOP', 'Paanga'), ('TRY', 'Turkish Lira'), ('TTD', 'Trinidad and Tobago Dollar'), ('TVD', 'Tuvalu dollar'), ('TWD', 'New Taiwan Dollar'), ('TZS', 'Tanzanian Shilling'), ('UAH', 'Hryvnia'), ('UGX', 'Uganda Shilling'), ('USD', 'US Dollar'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistan Sum'), ('VEF', 'Bolivar Fuerte'), ('VND', 'Dong'), ('VUV', 'Vatu'), ('WST', 'Tala'), ('XAF', 'CFA franc BEAC'), ('XAG', 'Silver'), ('XAU', 'Gold'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XCD', 'East Caribbean Dollar'), ('XDR', 'SDR'), ('XFO', 'Gold-Franc'), ('XFU', 'UIC-Franc'), ('XOF', 'CFA Franc BCEAO'), ('XPD', 'Palladium'), ('XPF', 'CFP Franc'), ('XPT', 'Platinum'), ('XTS', 'Codes specifically reserved for testing purposes'), ('XYZ', 'Default currency.'), ('YER', 'Yemeni Rial'), ('ZAR', 'Rand'), ('ZMK', 'Kwacha'), ('ZWD', 'Zimbabwe Dollar A/06'), ('ZWL', 'Zimbabwe dollar A/09'), ('ZWN', 'Zimbabwe dollar A/08')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='device',
            field=models.ForeignKey(related_name='contributions', to='devices.Device', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contribution',
            name='location',
            field=models.ForeignKey(related_name='contributions', to='main.Location', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plan',
            name='duration',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
