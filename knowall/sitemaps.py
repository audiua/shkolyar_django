from django.contrib.sitemaps import Sitemap
from .models import KnowallCategory, Knowall
from django.core.urlresolvers import reverse
import time
import arrow

class KnowallSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['knowall:index']

    def location(self, obj):
        return reverse(obj)

class KnowallCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return KnowallCategory.objects\
        .filter(articles__public=1, articles__public_time__lte=time.time())\
        .distinct()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)


class KnowallArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return Knowall.published.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)