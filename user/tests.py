from django import urls
from django.contrib.auth import models
from rest_framework import status, test

# Create your tests here.


class UserTests(test.APITestCase):

    def setUp(self):
        models.User.objects.create_user(username='Test1', password='testing1')
        models.User.objects.create_user(username='Test2', password='testing2')

    def test_get_current_user(self):
        url = urls.reverse('users-me')
        self.client.force_authenticate(user=models.User.objects.get(
            username='Test1'))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)
        self.assertEqual(response.data.get('username'), 'Test1')

    def test_patch_current_user(self):
        url = urls.reverse('users-me')
        self.client.force_authenticate(user=models.User.objects.get(
            username="Test1"))
        data = {'first_name': 'test_name'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         response.data)
        self.assertEqual(response.data.get('first_name'), 'test_name')

    def test_delete_current_user(self):
        url = urls.reverse('users-me')
        self.client.force_authenticate(user=models.User.objects.get(
            username='Test1'))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         response.data)
