# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models
import unixtimestampfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
                ('update_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('public_time', unixtimestampfield.fields.UnixTimeStampField(default=1493058114)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('nausea', models.FloatField(blank=True, null=True)),
                ('public', models.BooleanField(default=False)),
                ('vk_img', models.TextField(blank=True, null=True)),
                ('vk_public_time', models.IntegerField(blank=True, null=True)),
                ('uri', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'library_author',
            },
        ),
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('uri', models.CharField(max_length=255, unique=True)),
                ('create_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
                ('update_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('public_time', unixtimestampfield.fields.UnixTimeStampField(default=1493058114)),
                ('img_ext', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('nausea', models.FloatField(blank=True, null=True)),
                ('public', models.BooleanField(default=False)),
                ('vk_img', models.TextField(blank=True, null=True)),
                ('vk_public_time', models.IntegerField(blank=True, null=True)),
                ('library_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_books', to='library.LibraryAuthor')),
            ],
            options={
                'db_table': 'library_book',
            },
            bases=(models.Model, main.models.ViewCounterModel),
        ),
    ]
