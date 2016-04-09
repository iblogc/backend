from django.contrib import admin
from .models import Account
from accounts import models

# Register your models here.

from django.contrib import admin
from gezbackend.utils import get_password,get_random_code
from rest_framework.authtoken.models import Token


class AccountAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.security = get_random_code(10)
        obj.password = get_password(obj.password, obj.security)
        obj.save()
        Token.objects.create(user=obj)



admin.site.register(Account, AccountAdmin)
admin.site.register(models.AccountAdmin)
admin.site.register(models.AccountAdminRole)
