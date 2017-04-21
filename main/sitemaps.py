from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class MainSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return ['main:index', 'main:about', 'main:contact', 'main:rightholder']

    def location(self, obj):
        return reverse(obj)