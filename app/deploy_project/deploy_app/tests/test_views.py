from django.test import TestCase, Client
from django.urls import reverse
from deploy_app.models import Person, Government, Enterprise
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_people_url = reverse('list-people')
        self.list_enterprises_url = reverse('list-enterprises')
        self.list_governments_url = reverse('list-governments')

    def test_people_list_GET(self):
        response = self.client.get(self.list_people_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deploy_app/list_item.html')

    def test_enterprises_list_GET(self):
        response = self.client.get(self.list_enterprises_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deploy_app/list_item.html')

    def test_governments_list_GET(self):
        response = self.client.get(self.list_governments_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deploy_app/list_item.html')
