from django.db import models
from main.models import BaseModel, PublishedManager, TimestampModel, PublishModel
from django.core.urlresolvers import reverse

class LibraryAuthor(TimestampModel, PublishModel):
    author = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    length = models.SmallIntegerField(blank=True, null=True)
    nausea = models.FloatField(blank=True, null=True)
    public = models.BooleanField(default=False)
    vk_img = models.TextField(blank=True, null=True)
    vk_public_time = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=255)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        db_table = 'library_author'

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('library:author', args=(self.slug,))


class LibraryBook(BaseModel, TimestampModel, PublishModel):
    img_ext = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    library_author = models.ForeignKey(LibraryAuthor, models.DO_NOTHING,
                                       blank=True, null=True, related_name="author_books")
    length = models.SmallIntegerField(blank=True, null=True)
    nausea = models.FloatField(blank=True, null=True)
    public = models.BooleanField(default=False)
    vk_img = models.TextField(blank=True, null=True)
    vk_public_time = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        db_table = 'library_book'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book', args=(self.library_author.slug, self.slug))
