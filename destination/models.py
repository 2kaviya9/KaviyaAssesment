from django.db import models

from account.models import Account
from destination.enums import HTTPMethods

# Create your models here.
class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length = 10, choices=HTTPMethods.choices())
    headers = models.JSONField()

    def __str__(self):
        return f"{self.account.account_name}"
   
