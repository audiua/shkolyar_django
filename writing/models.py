from django.db import models
from django.core.urlresolvers import reverse
from main.models import BaseModel, TimestampModel, PublishModel, PublishedManager, ViewCounterModel
from unixtimestampfield.fields import UnixTimeStampField

class Writing(BaseModel, TimestampModel, PublishModel, ViewCounterModel):
    clas = models.ForeignKey('WritingClas', models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('WritingSubject', models.DO_NOTHING, blank=True, null=True, related_name='subject_writings')
    text = models.TextField()
    length = models.SmallIntegerField()
    nausea = models.FloatField()
    thumbnail_ext = models.CharField(max_length=255, blank=True, null=True)
    public = models.BooleanField()
    vk_img = models.TextField(blank=True, null=True)
    vk_public_time = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        db_table = 'writing'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('writing:article', args=(self.clas.slug,
                                                self.subject.slug,
                                                self.slug))

    def save(self, *args, **kwargs):
        self.uri = reverse('writing:article', args={self.clas.slug, self.subject.slug, self.slug})
        super(Writing, self).save(*args, **kwargs)


class WritingClas(BaseModel, TimestampModel):
    class Meta:
        db_table = 'writing_clas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('writing:clas', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.uri = reverse('writing:clas', args={self.slug})
        super(WritingClas, self).save(*args, **kwargs)


class WritingSubject(BaseModel, TimestampModel):
    writing_clas = models.ForeignKey(WritingClas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'writing_subject'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('writing:subject', args=(self.writing_clas.slug, self.slug))

    def save(self, *args, **kwargs):
        self.uri = reverse('writing:subject', args={self.clas.slug, self.slug})
        super(WritingSubject, self).save(*args, **kwargs)
