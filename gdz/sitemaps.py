from django.contrib.sitemaps import Sitemap
from .models import GdzBook, GdzClas, GdzSubject
from django.core.urlresolvers import reverse
import time
import datetime
import arrow

class GdzSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ['gdz:index']

    def location(self, obj):
        return reverse(obj)

class GdzClasSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return GdzClas.objects.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)

class GdzSubjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return GdzSubject.objects.filter(gdz_subject_books__public=1,
                                             gdz_subject_books__lte=int(time.time()))

    def lastmod(self, obj):
        return arrow.get(obj.update_time)

class GdzBookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return GdzBook.published.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time).to('local')