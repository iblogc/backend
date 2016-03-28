from django.contrib import admin
from .models import Account

# Register your models here.

from django.contrib import admin
from gezbackend.utils import get_password

class AccountAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = get_password(obj.password,obj.security)
        obj.save()

admin.site.register(Account, AccountAdmin)