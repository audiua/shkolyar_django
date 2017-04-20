import time
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import EmptyPage, Paginator
from .models import GdzBook, GdzSubject, GdzClas

PAGE_ITEM = 12

# @cache_page(60 * 1)
def index(request, page=1):
    """
    Список гдз сборников
    """
    book_list = GdzBook.objects.filter(public=1, public_time__lte=int(time.time()))\
        .order_by('-public_time')
    paginator = Paginator(book_list, PAGE_ITEM)
    try:
        books = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "ГДЗ (Готові домашні завдання)"
    page_title = "ГДЗ (Готові домашні завдання)"

    return render(request, 'gdz/index.html', {'books': books,
                                              'h1': h1,
                                              'page_title': page_title,
                                              'paginate_link': 'gdz:index_paginate',
                                              'link': 'gdz:index',
                                              'page': page})


def classes_list(request, clas_slug, page=1):
    """
    Список гдз сборников для класа
    """
    gdz_clas = get_object_or_404(GdzClas, slug=clas_slug)
    book_list = GdzBook.published.filter(gdz_clas=gdz_clas).order_by('-public_time')
    paginator = Paginator(book_list, PAGE_ITEM)
    try:
        books = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Гдз {clas_slug} клас".format(clas_slug=gdz_clas.slug)
    page_title = "Гдз {clas_slug} клас".format(clas_slug=gdz_clas.slug)

    return render(request, 'gdz/clas.html', {'books': books,
                                             'h1': h1,
                                             'page_title': page_title,
                                             'gdz_clas': gdz_clas,
                                             'paginate_link': 'gdz:clas_paginate',
                                             'link': 'gdz:clas'})

def subject(request, clas_slug, subject_slug, page=1):
    """
    Список гдз сборников для предмета
    """
    gdz_clas = get_object_or_404(GdzClas, slug=clas_slug)
    gdz_subject = get_object_or_404(GdzSubject, slug=subject_slug, gdz_clas=gdz_clas)
    book_list = GdzBook.published.filter(gdz_clas=gdz_clas,
                                         gdz_subject=gdz_subject).order_by('-public_time')
    paginator = Paginator(book_list, PAGE_ITEM)
    try:
        books = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Гдз {subject_title} {clas_slug} клас".format(subject_title=gdz_subject.title,
                                                       clas_slug=gdz_clas.slug)
    page_title = "Гдз {subject_title} {clas_slug} клас".format(subject_title=gdz_subject.title,
                                                       clas_slug=gdz_clas.slug)


    return render(request, 'gdz/subject.html', {'books': books, 'h1': h1,
                                                'page_title': page_title,
                                                'gdz_clas': gdz_clas,
                                                'gdz_subject': gdz_subject,
                                                'paginate_link': 'gdz:subject_paginate',
                                                'link': 'gdz:subject'})

def book(request, clas_slug, subject_slug, book_slug):
    gdz_clas = get_object_or_404(GdzClas, slug=clas_slug)
    gdz_subject = get_object_or_404(GdzSubject, slug=subject_slug, gdz_clas=gdz_clas)
    gdz_book = get_object_or_404(GdzBook, gdz_clas=gdz_clas, gdz_subject=gdz_subject,
                                 slug=book_slug, public=1, public_time__lte=time.time())
    return render(request, 'gdz/detail_book.html', {'gdz_book': gdz_book,
                                                    'gdz_subject': gdz_subject, 'gdz_clas': gdz_clas})

def task(request, book_slug, task_number):
    pass