from django.test import TestCase
from gdz.models import GdzClas
from django.test import Client
from rest_framework.reverse import reverse


class TestGdzApiClas(TestCase):
    fixtures = ['gdz_clas.json']

    def test_clas_api_detail(self):
        clases = GdzClas.objects.all()
        client = Client()
        for clas in clases:
            response = client.get(reverse('gdz_api:gdzclas-detail', args={clas.id}))
            self.assertEqual(response.status_code, 200)

    def test_clas_api_list(self):
        client = Client()
        response = client.get(reverse('gdz_api:gdzclas-list', args={}))
        self.assertEqual(response.status_code, 200)

