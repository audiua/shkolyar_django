from django.test import TestCase
from gdz.models import GdzSubject
from django.test import Client
from django.core.urlresolvers import reverse


class TestGdzSubject(TestCase):
    fixtures = ['gdz_clas.json', 'gdz.json']

    def test_subject_view(self):
        subjects = GdzSubject.objects.all()
        client = Client()
        for subject in subjects:
            response = client.get(reverse('gdz:subject', args=(subject.gdz_clas.slug,
                                                               subject.slug)))
            self.assertEqual(response.status_code, 200)