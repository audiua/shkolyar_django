from django.contrib.sitemaps import Sitemap
from .models import Writing, WritingClas, WritingSubject
from django.core.urlresolvers import reverse
import time
import arrow


class WritingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['writing:index']

    def location(self, obj):
        return reverse(obj)


class WritingClasSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return WritingClas.objects.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)


class WritingSubjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return WritingSubject.objects.filter(subject_writings__public=1,
                                             subject_writings__public_time__lte=time.time())

    def lastmod(self, obj):
        return arrow.get(obj.update_time)

class WritingArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.2

    def items(self):
        return Writing.published.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)