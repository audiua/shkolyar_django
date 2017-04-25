from django.test import TestCase
from gdz.models import GdzSubject
from django.test import Client
from rest_framework.reverse import reverse


class TestGdzApiClas(TestCase):
    fixtures = ['gdz_clas.json', 'gdz.json']

    def setUp(self):
        self.client = Client()

    def test_clas_api_detail(self):
        subjects = GdzSubject.objects.all()
        for subject in subjects:
            response = self.client.get(reverse('gdz_api:gdzsubject-detail', args={subject.pk}))
            self.assertEqual(response.status_code, 200)

    def test_clas_api_list(self):
        client = Client()
        response = self.client.get(reverse('gdz_api:gdzsubject-list'))
        self.assertEqual(response.status_code, 200)

