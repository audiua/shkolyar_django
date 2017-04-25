"""shkolyar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from gdz import sitemaps as gdz_sitemap
from knowall import sitemaps as knowall_sitemap
from library import sitemaps as library_sitemap
from main import sitemaps as main_sitemaps
from textbook import sitemaps as textbook_sitemap
from writing import sitemaps as writing_sitemap

sitemaps = {
    'gdz': gdz_sitemap.GdzSitemap,
    'gdz_clas': gdz_sitemap.GdzClasSitemap,
    'gdz_subject': gdz_sitemap.GdzSubjectSitemap,
    'gdz_book': gdz_sitemap.GdzBookSitemap,
    'knowall': knowall_sitemap.KnowallSitemap,
    'knowall_category': knowall_sitemap.KnowallCategorySitemap,
    'knowall_article': knowall_sitemap.KnowallArticleSitemap,
    'library': library_sitemap.LibrarySitemap,
    'library_author': library_sitemap.LibraryAuthorSitemap,
    'library_article': library_sitemap.LibraryBookSitemap,
    'main': main_sitemaps.MainSitemap,
    'textbook': textbook_sitemap.TextbookSitemap,
    'textbook_clas': textbook_sitemap.TextbookClasSitemap,
    'textbook_subject': textbook_sitemap.TextbookSubjectSitemap,
    'textbook_book': textbook_sitemap.TextbookBookSitemap,
    'writing': writing_sitemap.WritingSitemap,
    'writing_clas': writing_sitemap.WritingClasSitemap,
    'writing_subject': writing_sitemap.WritingSubjectSitemap,
    'writing_article': writing_sitemap.WritingArticleSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/gdz/', include('gdz.urls', namespace='gdz_api')),
    url(r'^gdz', include('gdz.urls', namespace='gdz')),
    url(r'^textbook', include('textbook.urls', namespace='textbook')),
    url(r'^writing', include('writing.urls', namespace='writing')),
    url(r'^knowall', include('knowall.urls', namespace='knowall')),
    url(r'^library', include('library.urls', namespace='library')),

    url(r'^sitemap\.xml$', cache_page(86400, cache="default")(sitemap) , {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),

    url(r'^', include('main.urls', namespace='main')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)