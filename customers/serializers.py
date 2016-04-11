# -*- encoding:utf-8 -*-

from rest_framework import serializers
from .models import CustomerAccount


class CustomerAccountSerializer(serializers.ModelSerializer):
    no = serializers.CharField(max_length=200,
                               allow_blank=True)
    source = serializers.IntegerField()
    username = serializers.CharField(max_length=200,
                                     allow_blank=True)
    password = serializers.CharField(max_length=50,
                                     allow_blank=True, write_only=True)
    role = serializers.IntegerField()
    active = serializers.BooleanField(default=True)
    register_date = serializers.DateField(format='%Y.%M.%d', input_formats='Y.M.d')
    avatar = serializers.ImageField(allow_empty_file=True)
    real_name = serializers.CharField(max_length=200,
                                      allow_blank=True)
    birth_date = serializers.DateField(format='%Y.%M.%d', input_formats='Y.M.d')
    phone = serializers.CharField(max_length=50,
                                  allow_blank=True)
    email = serializers.EmailField(max_length=200,
                                   allow_blank=True)
    # 认证
    certified = serializers.BooleanField(default=False)
    # 审核
    approved = serializers.BooleanField(default=False)

    register_no = serializers.CharField(max_length=50,
                                        allow_blank=True)
    cert_no = serializers.CharField(max_length=50,
                                    allow_blank=True)
    bank_no = serializers.CharField(max_length=50,
                                    allow_blank=True)
    business_license = serializers.FileField(
        allow_empty_file=True)

    class Meta:
        model = CustomerAccount
        fields = (
            'id', 'no', 'source', 'username', 'password', 'role', 'active',
            'register_date', 'avatar', 'real_name', 'birth_date', 'phone',
            'email',
            'certified', 'approved', 'register_no', 'cert_no', 'bank_no',
            'business_license')
