from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class RecipeTests(APITestCase):

    def test_get_recipe(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)