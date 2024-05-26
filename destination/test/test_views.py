from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from account.models import Account
from destination.models import Destination
from destination.enums import HTTPMethods

class DestinationAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.account = Account.objects.create(
            username='testuser', 
            password='testpassword',
            email='testuser@example.com',
            account_id='account_123',
            account_name='Test Account'
        )
        self.destination = Destination.objects.create(
            account=self.account,
            url='https://example.com',
            http_method=HTTPMethods.GET.value,
            headers={'Content-Type': 'application/json'}
        )
        self.destination_url = reverse('destination-detail', kwargs={'pk': self.destination.pk})
        self.destination_list_url = reverse('destination-list')

    def test_create_destination(self):
        data = {
            'account': self.account.pk,
            'url': 'https://newexample.com',
            'http_method': HTTPMethods.POST.value,
            'headers': {'Content-Type': 'application/json'}
        }
        response = self.client.post(self.destination_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['url'], 'https://newexample.com')
        self.assertEqual(response.data['http_method'], HTTPMethods.POST.value)

    def test_get_destination(self):
        response = self.client.get(self.destination_url, format='application/json')
        print(response.data['http_method'], "************************")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://example.com')
        self.assertEqual(response.data['http_method'], HTTPMethods.GET.value)

    def test_update_destination(self):
        data = {
            'url': 'https://updatedexample.com',
            'http_method': HTTPMethods.PUT.value,
            'headers': {'Content-Type': 'json'},
            'account': self.account.pk
        }
        response = self.client.put(self.destination_url, data, format='json')
        print(response.content, "&&&&&&&&&&&&&&&&&&&")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://updatedexample.com')
        self.assertEqual(response.data['http_method'], HTTPMethods.PUT.value)

    def test_delete_destination(self):
        response = self.client.delete(self.destination_url, format='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Destination.objects.filter(pk=self.destination.pk).exists())
