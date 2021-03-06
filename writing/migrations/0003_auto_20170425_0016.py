# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0002_auto_20170425_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writing',
            name='public_time',
            field=unixtimestampfield.fields.UnixTimeStampField(default=1493068593),
        ),
        migrations.AlterField(
            model_name='writing',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='writingclas',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='writingsubject',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
