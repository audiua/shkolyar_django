from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import EmptyPage, Paginator
from .models import LibraryAuthor, LibraryBook
import time

PAGE_ITEM = 24

def index(request, page=1):
    authors = LibraryAuthor.published.order_by('author')
    paginator = Paginator(authors, PAGE_ITEM)
    try:
        authors = paginator.page(page)
    except EmptyPage:
        raise Http404

    h1 = "Література"
    page_title = "Література"

    return render(request, 'library/index.html', {'authors': authors,
                                                  'h1': h1,
                                                  'page_title': page_title,
                                                  'paginate_link': 'library:index_paginate',
                                                  'link': 'library:index',
                                                  'page': page})

def author(request, author_slug):
    author = get_object_or_404(LibraryAuthor, slug=author_slug, public=1, public_time__lte=float(time.time()))

    h1 = author.author
    page_title = author.author

    return render(request, 'library/author.html', {'author': author,
                                                  'h1': h1,
                                                  'page_title': page_title})


def book(request, author_slug, book_slug):
    author = get_object_or_404(LibraryAuthor, slug=author_slug)
    book = get_object_or_404(LibraryBook, slug=book_slug, library_author=author, public=1,
                             public_time__lte=int(time.time()))

    h1 = book.title
    page_title = book.title

    return render(request, 'library/book.html', {'book': book,
                                                 'author': author,
                                                 'h1': h1,
                                                 'page_title': page_title})
