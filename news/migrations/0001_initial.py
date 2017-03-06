# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('newsId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
