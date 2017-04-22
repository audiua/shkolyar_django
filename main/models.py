from django.db import models
from datetime import datetime
from unixtimestampfield.fields  import UnixTimeStampField
import time
from django.core.urlresolvers import reverse

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

    create_time = UnixTimeStampField(auto_now_add=True)
    update_time = UnixTimeStampField(auto_now=True)

class PublishModel(models.Model):
    class Meta:
        abstract = True

    public_time = UnixTimeStampField(use_numeric=True, default=int(time.time()))

class ViewCount(models.Model):
    """
    View count model
    """
    model = models.CharField(max_length=55, default='model')
    counter = models.IntegerField(default=1)
    uri = models.CharField(max_length=255)

    class Meta:
        db_table = 'view_count'

class ViewCounterModel(object):
    """
    mixin view_count method
    """
    def view_count(self):
        counter = ViewCount.objects.get(uri=self.get_absolute_url())
        if counter:
            return counter.counter
        return 1