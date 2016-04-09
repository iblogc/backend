# -*- encoding:utf-8 -*-

from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    security = serializers.CharField(max_length=50,read_only=True)
    email = serializers.EmailField()

    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'email', 'security')