# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_store_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='prize',
            field=models.IntegerField(),
        ),
    ]
