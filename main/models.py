from django.db import models
from datetime import datetime
from unixtimestampfield.fields  import UnixTimeStampField
import time

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(public=1,
                                                    public_time__lte=int(time.time()))

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


