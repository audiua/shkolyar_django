from django.db import models
from unixtimestampfield.fields  import UnixTimeStampField

class Banner(models.Model):
    title = models.CharField(max_length=255)
    refresh = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    type = models.CharField(max_length=255)
    code = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'banner'


class BannerCode(models.Model):
    code = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    view_count = models.IntegerField(blank=True, null=True)
    banner = models.ForeignKey(Banner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'banner_code'


class Place(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    created_at = UnixTimeStampField(auto_now_add=True)
    updated_at = UnixTimeStampField(auto_now=True)
    refresh = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    entity = models.CharField(max_length=255, blank=True, null=True)
    banner = models.ManyToManyField(Banner, through='PlaceBanner', verbose_name='books')

    class Meta:
        db_table = 'place'


class PlaceBanner(models.Model):
    place = models.ForeignKey(Place, models.DO_NOTHING)
    banner = models.ForeignKey(Banner, models.DO_NOTHING)

    class Meta:
        db_table = 'place_banner'
