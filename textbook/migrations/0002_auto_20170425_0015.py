# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbookbook',
            name='create_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='textbookbook',
            name='public_time',
            field=unixtimestampfield.fields.UnixTimeStampField(default=1493068531),
        ),
        migrations.AlterField(
            model_name='textbookbook',
            name='update_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='textbookclas',
            name='create_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='textbookclas',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='textbookclas',
            name='update_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='textbooksubject',
            name='create_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='textbooksubject',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='textbooksubject',
            name='update_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now=True, default=0.0),
        ),
    ]
