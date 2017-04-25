from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clases', views.GdzClasViewSet)
router.register(r'subjects', views.GdzSubjectViewSet)
router.register(r'books', views.GdzBookViewSet)


urlpatterns = [

#api endpoint
    url(r'^', include(router.urls)),


    url(r'^/(?P<clas_slug>\d{1,2})/(?P<subject_slug>[-_a-z]+)/page/(?P<page>\d+)$',
        views.subject, name='subject_paginate'),
    url(r'^(?P<clas_slug>\d{1,2})/page/(?P<page>\d+)$', views.classes_list, name='clas_paginate'),

    url(r'^/(?P<clas_slug>\d{1,2})/(?P<subject_slug>[-_a-z]+)/(?P<book_slug>[-_a-z0-9]+)$',
        views.book, name='book'),

    # ссылка на страницу предмета с пагинацией
    url(r'^/(?P<clas_slug>\d{1,2})/(?P<subject_slug>[-_a-z]+)$',
        views.subject, name='subject'),
    # страничка класа с пагинацией и без

    url(r'^/(?P<clas_slug>\d{1,2})$', views.classes_list, name='clas'),

    url(r'^/page/(?P<page>\d+)$', views.index, name='index_paginate'),



    url(r'^$', views.index, name='index'),
]