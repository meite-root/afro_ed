# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0006_typify_alt_names_and_add_is_historic'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currency_symbol',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='postal_code_format',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='postal_code_regex',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='currency_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
