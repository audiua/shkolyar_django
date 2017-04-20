from django.db import models
from datetime import datetime
from unixtimestampfield.fields import UnixTimeStampField

class BaseModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    uri = models.CharField(max_length=255, unique=True)

class TimestampModel(models.Model):
    class Meta:
        abstract = True

    create_time = UnixTimeStampField(auto_now_add=True, use_numeric=True)
    update_time = UnixTimeStampField(auto_now=True, use_numeric=True)

class PublishModel(models.Model):
    class Meta:
        abstract = True

    public_time = UnixTimeStampField(auto_now_add=True, use_numeric=True)


