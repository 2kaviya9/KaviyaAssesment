from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import Account
from destination.models import Destination
from destination.enums import HTTPMethods

class DestinationModelTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            username='testuser', 
            password='testpassword',
            account_name='Test Account'
        )
        self.destination = Destination.objects.create(
            account=self.account,
            url='https://example.com',
            http_method=HTTPMethods.GET,
            headers={'Content-Type': 'application/json'}
        )

    def test_destination_creation(self):
        self.assertIsInstance(self.destination, Destination)
        self.assertEqual(self.destination.url, 'https://example.com')
        self.assertEqual(self.destination.http_method, HTTPMethods.GET)
        self.assertEqual(self.destination.headers, {'Content-Type': 'application/json'})
        self.assertEqual(self.destination.account.account_name, 'Test Account')

    def test_str_method(self):
        self.assertEqual(str(self.destination), 'Test Account')
