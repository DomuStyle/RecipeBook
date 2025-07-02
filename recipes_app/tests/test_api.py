from django.urls import reverse
from django.contrib.auth.models import User
from recipes_app.models import Recipe

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class RecipeAPITestCaseHappy(APITestCase): 
        
    def setUp(self): 
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.recipe = Recipe.objects.create(title='Recipe1',description='description',author=self.user)

        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_recipe(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_post_recipe(self):
        url = reverse('recipe-list')
        data = {
            'title':'Recipe1',
            'description':'description',
            'author':self.user.id
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_recipe(self):
        url = reverse('recipe-detail', kwargs={'pk': self.recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RecipeAPITestCaseUnhappy(APITestCase): 
        
    def setUp(self): 
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.recipe = Recipe.objects.create(title='Recipe1',description='description',author=self.user)

    def test_list_unauthenticated_post_recipe(self):
        url = reverse('recipe-list')
        data = {
            'title':'Recipe1',
            'description':'description',
            'author':self.user.id
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)     


    def test_unauthenticated_detail_recipe(self):
        url = reverse('recipe-detail', kwargs={'pk': self.recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)   


