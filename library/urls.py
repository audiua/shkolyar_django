from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<author_slug>[-a-z0-9]+)/(?P<book_slug>[-a-z0-9]+)$',
        views.book, name='book'),
    url(r'^(?P<author_slug>[-a-z0-9]+)$', views.author, name='author'),

    url(r'^page/(?P<page>\d+)$', views.index, name='index_paginate'),
    url(r'^$', views.index, name='index'),
]