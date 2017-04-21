from django.contrib.sitemaps import Sitemap
from .models import TextbookBook, TextbookClas, TextbookSubject
from django.core.urlresolvers import reverse
import time
import arrow

class TextbookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['textbook:index']

    def location(self, obj):
        return reverse(obj)

class TextbookClasSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return TextbookClas.objects.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)

class TextbookSubjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return TextbookSubject.objects.filter(subject_textbooks__public=1,
                                             subject_textbooks__lte=time.time())

    def lastmod(self, obj):
        return arrow.get(obj.update_time)

class TextbookBookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.2

    def items(self):
        return TextbookBook.published.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)