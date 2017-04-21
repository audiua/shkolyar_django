from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<category_slug>[-a-z0-9]+)/(?P<article_slug>[-a-z0-9]+)$',
        views.article, name='article'),

    url(r'^(?P<category_slug>[-a-z0-9]+)/page/(?P<page>\d+)/$',
        views.category, name='category_index'),
    url(r'^(?P<category_slug>[-a-z0-9]+)/$', views.category, name='category'),

    url(r'^page/(?P<page>\d+)/$', views.index, name='index_paginate'),
    url(r'^$', views.index, name='index'),
]