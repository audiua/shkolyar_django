import time
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import EmptyPage, Paginator
from .models import Knowall, KnowallCategory

PAGE_ITEM = 12

def index(request, page=1):
    articles = Knowall.published.order_by('-public_time')
    paginator = Paginator(articles, PAGE_ITEM)
    try:
        articles = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Всезнайка"
    page_title = "Всезнайка"

    return render(request, 'knowall/index.html', {'articles': articles,
                                              'h1': h1,
                                              'page_title': page_title,
                                              'paginate_link': 'knowall:index_paginate',
                                              'link': 'knowall:index',
                                              'page': page})


def category(request, category_slug, page=1):
    category = get_object_or_404(KnowallCategory, slug=category_slug)
    articles = Knowall.published.filter(knowall_category=category).order_by('-public_time')
    paginator = Paginator(articles, PAGE_ITEM)
    try:
        articles = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Всезнайка {}".format(category.title)
    page_title = "Всезнайка {}".format(category.title)

    return render(request, 'knowall/category.html', {'articles': articles,
                                                  'category': category,
                                                  'h1': h1,
                                                  'page_title': page_title,
                                                  'paginate_link': 'knowall:category_paginate',
                                                  'link': 'knowall:category',
                                                  'page': page})

def article(request, category_slug, article_slug):
    category = get_object_or_404(KnowallCategory, slug=category_slug)
    article = get_object_or_404(Knowall, slug=article_slug, knowall_category=category, public=1, public_time__lte=time.time())

    h1 = article.title
    page_title = article.title

    return render(request, 'knowall/article.html', {'article': article, 'category': category,
                                                    'h1': h1, 'page_title': page_title})