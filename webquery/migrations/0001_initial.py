# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
    ]
