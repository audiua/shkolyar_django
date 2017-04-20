from django.shortcuts import render, get_object_or_404
from .models import TextbookBook, TextbookClas, TextbookSubject
from django.http import Http404
from django.core.paginator import EmptyPage, Paginator
import time

PAGE_ITEM = 12

def index(request, page=1):
    """
        Список учебников
        """
    book_list = TextbookBook.published.order_by('-public_time')
    paginator = Paginator(book_list, PAGE_ITEM)
    try:
        books = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Підручники"
    page_title = "Підручники онлайн"

    return render(request, 'textbook/index.html', {'books': books,
                                              'h1': h1,
                                              'page_title': page_title,
                                              'paginate_link': 'textbook:index_paginate',
                                              'link': 'textbook:index',
                                              'page': page})

def clas(request, clas_slug, page=1):
    textbook_clas = get_object_or_404(TextbookClas, slug=clas_slug)
    book_list = TextbookBook.published.filter(textbook_clas=textbook_clas).order_by('-public_time')
    paginator = Paginator(book_list, PAGE_ITEM)
    try:
        books = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Підручники {clas_slug} клас".format(clas_slug=textbook_clas.name)
    page_title = "Підручники {clas_slug} клас".format(clas_slug=textbook_clas.name)

    return render(request, 'textbook/clas.html', {'books': books,
                                             'h1': h1,
                                             'page_title': page_title,
                                             'textbook_clas': textbook_clas,
                                             'paginate_link': 'textbook:clas_paginate',
                                             'link': 'textbook:clas'})


def subject(request, clas_slug, subject_slug, page=1):
    textbook_clas = get_object_or_404(TextbookClas, slug=clas_slug)
    textbook_subject = get_object_or_404(TextbookSubject, slug=subject_slug, textbook_clas=textbook_clas)
    book_list = TextbookBook.published.filter(textbook_clas=textbook_clas,
                                         textbook_subject=textbook_subject).order_by('-public_time')
    paginator = Paginator(book_list, PAGE_ITEM)
    try:
        books = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Гдз {subject_title} {clas_slug} клас".format(subject_title=textbook_subject.title,
                                                       clas_slug=textbook_clas.name)
    page_title = "Гдз {subject_title} {clas_slug} клас".format(subject_title=textbook_subject.title,
                                                               clas_slug=textbook_clas.slug)

    return render(request, 'textbook/subject.html', {'books': books, 'h1': h1,
                                                'page_title': page_title,
                                                'textbook_clas': textbook_clas,
                                                'textbook_subject': textbook_subject,
                                                'paginate_link': 'textbook:subject_paginate',
                                                'link': 'textbook:subject'})

def book(request, clas_slug, subject_slug, book_slug):
    textbook_clas = get_object_or_404(TextbookClas, slug=clas_slug)
    textbook_subject = get_object_or_404(TextbookSubject, slug=subject_slug, textbook_clas=textbook_clas)
    textbook_book = get_object_or_404(TextbookBook, textbook_clas=textbook_clas, textbook_subject=textbook_subject,
                                 slug=book_slug, public=1, public_time__lte=time.time())
    return render(request, 'textbook/detail_book.html', {'textbook_book': textbook_book,
                                                    'textbook_subject': textbook_subject, 'textbook_clas': textbook_clas})


