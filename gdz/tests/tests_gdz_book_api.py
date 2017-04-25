from django.test import TestCase
from gdz.models import GdzBook
from django.test import Client
from rest_framework.reverse import reverse


class TestGdzBookApi(TestCase):
    fixtures = ['gdz_clas.json', 'gdz.json']

    def setUp(self):
        self.client = Client()

    def test_gdz_book_api_detail(self):
        books = GdzBook.published.all()
        for book in books:
            response = self.client.get(reverse('gdz_api:gdzbook-detail', args={book.id}))
            self.assertEqual(response.status_code, 200)

    def test_gdz_book_api_list(self):
        response = self.client.get(reverse('gdz_api:gdzbook-list'))
        self.assertEqual(response.status_code, 200)

