from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import random

"""
Here Account model link with auth User model because of get app_secret_token in login response
"""
class Account(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    account_id = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=50)
    app_secret_token = models.CharField(max_length=50, unique=True)  # Automatically generated
    website = models.URLField(null=True)

    groups = models.ManyToManyField(Group, related_name='account_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_user_set', blank=True)

    def clean(self):
        # Generate a unique random integer for app_secret_token
        while True:
            random_int = random.randint(1, 10000)
            existing_obj = Account.objects.filter(app_secret_token=random_int).first()
            if not existing_obj:
                break
        self.app_secret_token = str(random_int)
        self.username = self.email.split("@")[0]

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.clean()  # Ensure clean is called to generate the token before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_name
    

