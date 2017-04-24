from django.test import TestCase
from gdz.models import GdzBook
from django.test import Client
from django.core.urlresolvers import reverse


class TestGdzBook(TestCase):
    fixtures = ['gdz_clas.json', 'gdz.json']

    def test_book_view(self):
        books = GdzBook.published.all()
        client = Client()
        for book in books:
            response = client.get(reverse('gdz:book', args={book.gdz_clas.slug,
                                                            book.gdz_subject.slug,
                                                            book.slug}))
            self.assertEqual(response.status_code, 200)