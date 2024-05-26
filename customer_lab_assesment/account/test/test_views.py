# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from account.models import Account

class AccountAPITestCase(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(
            email='test@example.com',
            account_id='12345',
            account_name='Test Account',
            app_secret_token='secret_token_12345',
            website='http://example.com'
        )
        self.valid_payload = {
            'email': 'newtest@example.com',
            'account_id': '54321',
            'account_name': 'New Test Account',
            'app_secret_token': 'secret_token_54321',
            'website': 'http://example.org'
        }
        self.invalid_payload = {
            'email': '',
            'account_id': '',
            'account_name': '',
            'app_secret_token': '',
            'website': ''
        }

    def test_create_account(self):
        url = reverse('account-list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_account_invalid(self):
        url = reverse('account-list')
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_account(self):
        url = reverse('account-detail', kwargs={'pk': self.account.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['account_name'], self.account.account_name)

    def test_update_account(self):
        url = reverse('account-detail', kwargs={'pk': self.account.pk})
        response = self.client.put(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        url = reverse('account-detail', kwargs={'pk': self.account.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
