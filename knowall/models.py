from django.db import models
from django.core.urlresolvers import reverse
from main.models import BaseModel, TimestampModel, PublishModel, PublishedManager


class Knowall(BaseModel, TimestampModel, PublishModel):
    text = models.TextField(blank=True, null=True)
    knowall_category = models.ForeignKey('KnowallCategory', models.DO_NOTHING, blank=True, null=True, related_name='articles')
    public = models.BooleanField(default=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_ext = models.CharField(max_length=255, blank=True, null=True)
    length = models.SmallIntegerField(blank=True, null=True)
    nausea = models.FloatField(blank=True, null=True)
    vk_img = models.TextField(blank=True, null=True)
    vk_public_time = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        db_table = 'knowall'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('knowall:article', args=(self.knowall_category.slug,
                                                self.slug))

class KnowallCategory(BaseModel, TimestampModel):
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'knowall_category'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('knowall:category', args=(self.slug,))


class KnowallGrab(models.Model):
    url = models.CharField(max_length=255)
    raw = models.TextField()
    content = models.TextField()
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    translate = models.TextField()
    checked = models.IntegerField(blank=True, null=True)
    translate_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'knowall_grab'

    def __str__(self):
        return self.title
