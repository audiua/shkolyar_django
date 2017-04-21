from django.contrib.sitemaps import Sitemap
from .models import LibraryAuthor, LibraryBook
from django.core.urlresolvers import reverse
import time
import arrow


class LibrarySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['library:index']

    def location(self, obj):
        return reverse(obj)


class LibraryAuthorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4

    def items(self):
        return LibraryAuthor.objects\
        .filter(author_books__public=1, author_books__public_time__lte=time.time())\
        .distinct()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)


class LibraryBookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
        return LibraryBook.published.all()

    def lastmod(self, obj):
        return arrow.get(obj.update_time)