from django.contrib import admin
from account.models import Account
# Register your models here.



class AccountAdmin(admin.ModelAdmin):
    list_display = ["id"]
admin.site.register(Account, AccountAdmin)


