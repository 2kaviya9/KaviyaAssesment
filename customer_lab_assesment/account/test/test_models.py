# account/tests.py
from django.test import TestCase
from account.models import Account

class TestAccountModel(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            email="test@gmail.com",
            account_id="11",
            account_name="test_account",
            website="http://example.com"
        )

    def test_account_creation(self):
        self.assertEqual(self.account.email, "test@gmail.com")
        self.assertEqual(self.account.account_id, "11")
        self.assertEqual(self.account.account_name, "test_account")
        self.assertEqual(self.account.website, "http://example.com")

    def test_email_unique(self):
        with self.assertRaises(Exception):
            Account.objects.create(
                email="test@gmail.com",
                account_id="12",
                account_name="test_account_2",
                app_secret_token="unique_token_2",
                website="http://example2.com"
            )

    def test_account_id_unique(self):
        with self.assertRaises(Exception):
            Account.objects.create(
                email="test2@gmail.com",
                account_id="11",
                account_name="test_account_2",
                website="http://example2.com"
            )

   
    def test_account_str_method(self):
        self.assertEqual(str(self.account), "test_account")

    def test_website_field_nullable(self):
        account_without_website = Account.objects.create(
            email="test2@gmail.com",
            account_id="13",
            account_name="test_account_3",
        )
        self.assertIsNone(account_without_website.website)

    def test_account_name_max_length(self):
        max_length = self.account._meta.get_field('account_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        max_length = self.account._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def test_account_id_max_length(self):
        max_length = self.account._meta.get_field('account_id').max_length
        self.assertEqual(max_length, 50)

    def test_app_secret_token_max_length(self):
        max_length = self.account._meta.get_field('app_secret_token').max_length
        self.assertEqual(max_length, 50)
