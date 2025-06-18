from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RecipeAPITestCase(APITestCase):

    # def setUp(self):
    #     self.user = User.objects.create_user(username='testuser', password='testpassword')
    #     self.token = Token.objects.create(user=self.user)

    def test_get_recipe(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)