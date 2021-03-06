# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gdz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gdzbook',
            name='create_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='gdzbook',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gdzbook',
            name='update_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='gdzclas',
            name='create_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='gdzclas',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gdzclas',
            name='update_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='gdzsubject',
            name='create_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='gdzsubject',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gdzsubject',
            name='update_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now=True, default=0.0),
        ),
    ]
