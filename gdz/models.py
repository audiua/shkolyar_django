import time
from django.db import models
from django.core.urlresolvers import reverse
from main.models import BaseModel, TimestampModel, PublishedManager, ViewCounterModel
from unixtimestampfield.fields import UnixTimeStampField

class GdzClas(BaseModel, TimestampModel):
    description = models.TextField(blank=True, null=True)
    is_promote = models.BooleanField(default=False)

    class Meta:
        db_table = 'gdz_clas'

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('gdz:clas', args=[self.slug])

    def __str__(self):
        return "{} клас".format(self.slug)

    def save(self, *args, **kwargs):
        self.uri = reverse('gdz:clas', args={self.slug})
        super(GdzClas, self).save(*args, **kwargs)

class GdzSubject(BaseModel, TimestampModel):
    description = models.TextField(blank=True, null=True)
    gdz_clas = models.ForeignKey(GdzClas, models.DO_NOTHING, blank=True, null=True, related_name="clas_subjects")
    is_promote = models.BooleanField()

    class Meta:
        db_table = 'gdz_subject'

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('gdz:subject', args=[self.gdz_clas.slug, self.slug])

    def __str__(self):
        return "{} {} клас".format(self.title, self.gdz_clas.slug)

    def save(self, *args, **kwargs):
        self.uri = reverse('gdz:subject', args={self.gdz_clas.slug, self.slug})
        super(GdzSubject, self).save(*args, **kwargs)


class GdzBook(BaseModel, TimestampModel, ViewCounterModel):
    author = models.CharField(max_length=255)
    gdz_clas = models.ForeignKey('GdzClas', models.DO_NOTHING, blank=True, null=True, related_name='gdz_clas_books')
    gdz_subject = models.ForeignKey('GdzSubject', models.DO_NOTHING, blank=True, null=True, related_name='gdz_subject_books')
    img = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    properties = models.CharField(max_length=255, blank=True, null=True)
    pagination = models.CharField(max_length=255, blank=True, null=True)
    public_time = UnixTimeStampField(auto_now_add=True, use_numeric=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    public = models.BooleanField()
    edition = models.CharField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    vk_img = models.IntegerField(blank=True, null=True)
    vk_public_time = UnixTimeStampField(blank=True, null=True, use_numeric=True)
    is_promote = models.BooleanField()

    class Meta:
        db_table = 'gdz_book'

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('gdz:book', args=[self.gdz_clas.slug, self.gdz_subject.slug, self.slug])

    def save(self, *args, **kwargs):
        self.uri = reverse('gdz:book', args={self.gdz_clas.slug, self.gdz_subject.slug, self.slug})
        super(GdzBook, self).save(*args, **kwargs)