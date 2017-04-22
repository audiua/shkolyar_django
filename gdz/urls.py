from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<clas_slug>\d{1,2})/(?P<subject_slug>[-_a-z]+)/page/(?P<page>\d+)$',
        views.subject, name='subject_paginate'),
    url(r'^(?P<clas_slug>\d{1,2})/page/(?P<page>\d+)$', views.classes_list, name='clas_paginate'),

    url(r'^(?P<clas_slug>\d{1,2})/(?P<subject_slug>[-_a-z]+)/(?P<book_slug>[-_a-z0-9]+)$',
        views.book, name='book'),

    # ссылка на страницу предмета с пагинацией
    url(r'^(?P<clas_slug>\d{1,2})/(?P<subject_slug>[-_a-z]+)$',
        views.subject, name='subject'),
    # страничка класа с пагинацией и без

    url(r'^(?P<clas_slug>\d{1,2})$', views.classes_list, name='clas'),

    url(r'^page/(?P<page>\d+)$', views.index, name='index_paginate'),
    url(r'^$', views.index, name='index'),
]