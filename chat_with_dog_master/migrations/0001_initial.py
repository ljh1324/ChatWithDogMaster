# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogFeed',
            fields=[
                ('feed', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('eat', models.BooleanField()),
            ],
        ),
    ]
