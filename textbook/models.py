from django.db import models
from django.core.urlresolvers import reverse
from main.models import BaseModel, TimestampModel, PublishModel
from unixtimestampfield.fields import UnixTimeStampField
import time


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(public=1,
                                                    public_time__lte=int(time.time()))

class TextbookBook(TimestampModel, PublishModel):
    textbook_clas = models.ForeignKey('TextbookClas', models.DO_NOTHING, blank=True, null=True, related_name="clas_textbooks")
    textbook_subject = models.ForeignKey('TextbookSubject', models.DO_NOTHING, blank=True, null=True, related_name="subject_textbooks")
    author = models.CharField(max_length=500)
    year = models.CharField(max_length=255, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=2, blank=True, null=True)
    edition = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    public = models.BooleanField()
    issue_id = models.TextField(blank=True, null=True)
    issue_embed = models.TextField(blank=True, null=True)
    vk_publish_time = UnixTimeStampField(use_numeric=True, default=0.0)
    img = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    is_promote = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)
    uri = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'textbook_book'

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return "{} {}".format(self.textbook_subject.title, self.author)


class TextbookClas(BaseModel, TimestampModel):
    name = models.CharField(max_length=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_promote = models.BooleanField()

    class Meta:
        db_table = 'textbook_clas'

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name


class TextbookSubject(BaseModel, TimestampModel):
    textbook_clas = models.ForeignKey(TextbookClas, models.DO_NOTHING, blank=True, null=True, related_name="clas_subjects")
    description = models.CharField(max_length=255, blank=True, null=True)
    is_promote = models.BooleanField()

    class Meta:
        db_table = 'textbook_subject'

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title
