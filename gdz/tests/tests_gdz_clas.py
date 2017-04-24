from django.test import TestCase
from gdz.models import GdzClas
from django.test import Client
from django.core.urlresolvers import reverse


class TestGdzClas(TestCase):
    fixtures = ['gdz_clas.json']

    def test_clas_view(self):
        clases = GdzClas.objects.all()
        client = Client()
        for clas in clases:
            response = client.get(reverse('gdz:clas', args={clas.slug}))
            self.assertEqual(response.status_code, 200)

