from django.test import TestCase
from django.urls import reverse, resolve
from deploy_app.views import people, governments, enterprises

class TestURLs(TestCase):
    """docstring for TestURLs."""

    def test_list_people_resolves(self):
        url = reverse(people)
        self.assertEquals(resolve(url).func, people)

    def test_list_governments_resolves(self):
        url = reverse(governments)
        self.assertEquals(resolve(url).func, governments)

    def test_list_enterprises_resolves(self):
        url = reverse(enterprises)
        self.assertEquals(resolve(url).func, enterprises)
