from .models import WritingClas, Writing, WritingSubject
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import EmptyPage, Paginator
import time


PAGE_ITEM = 12

def index(request, page=1):
    articles = Writing.published.order_by('-public_time')
    paginator = Paginator(articles, PAGE_ITEM)
    try:
        articles = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Твори"
    page_title = "Твори"

    return render(request, 'writing/index.html', {'articles': articles,
                                              'h1': h1,
                                              'page_title': page_title,
                                              'paginate_link': 'writing:index_paginate',
                                              'link': 'writing:index',
                                              'page': page})

def clas(request, clas_slug, page=1):
    clas = get_object_or_404(WritingClas, slug=clas_slug)
    articles = Writing.published.filter(clas=clas)

    paginator = Paginator(articles, PAGE_ITEM)
    try:
        articles = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Твори {} клас".format(clas.slug)
    page_title = "Твори {} клас".format(clas.slug)

    return render(request, 'writing/clas.html', {'articles': articles,
                                                  'h1': h1,
                                                  'clas': clas,
                                                  'page_title': page_title,
                                                  'paginate_link': 'writing:clas_paginate',
                                                  'link': 'writing:clas',
                                                  'page': page})

def subject(request, clas_slug, subject_slug, page=1):
    clas = get_object_or_404(WritingClas, slug=clas_slug)
    subject = get_object_or_404(WritingSubject, slug=subject_slug, writing_clas=clas)
    articles = Writing.published.filter(clas=clas, subject=subject)

    paginator = Paginator(articles, PAGE_ITEM)
    try:
        articles = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Твори {} клас {}".format(clas.slug, subject.title)
    page_title = "Твори {} клас {} ".format(clas.slug, subject.title)

    return render(request, 'writing/subject.html', {'articles': articles,
                                                  'h1': h1,
                                                  'clas': clas,
                                                  'subject': subject,
                                                  'page_title': page_title,
                                                  'paginate_link': 'writing:subject_paginate',
                                                  'link': 'writing:subject',
                                                  'page': page})

def article(request, clas_slug, subject_slug, article_slug):
    clas = get_object_or_404(WritingClas, slug=clas_slug)
    subject = get_object_or_404(WritingSubject, slug=subject_slug, writing_clas=clas)
    article = get_object_or_404(Writing, clas=clas, subject=subject,
                                public=1, public_time__lte=time.time(), slug=article_slug)
    h1 = article.title
    page_title = article.title

    return render(request, 'writing/article.html', {'article': article,
                                                    'h1': h1,
                                                    'clas': clas,
                                                    'subject': subject,
                                                    'page_title': page_title})