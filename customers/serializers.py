# -*- encoding:utf-8 -*-

from rest_framework import serializers
from .models import CustomerAccount, PendingApprove, ApproveLog


class CustomerAccountSerializer(serializers.ModelSerializer):
    no = serializers.CharField(max_length=200,
                               allow_blank=True, allow_null=True)
    source = serializers.ChoiceField(choices=CustomerAccount.SOURCE_CHOICES)
    username = serializers.CharField(max_length=200,
                                     allow_blank=True, allow_null=True)
    password = serializers.CharField(max_length=50,
                                     allow_blank=True, allow_null=True,
                                     write_only=True)
    role = serializers.ChoiceField(choices=CustomerAccount.ROLE_CHOICES)
    active = serializers.BooleanField(default=True)
    register_date = serializers.DateTimeField()
    avatar = serializers.ImageField(allow_empty_file=True,allow_null=True)
    real_name = serializers.CharField(max_length=200,
                                      allow_blank=True, allow_null=True)
    gender = serializers.ChoiceField(choices=CustomerAccount.GENDER_CHOICES)
    birth_date = serializers.DateField()
    phone = serializers.CharField(max_length=50,
                                  allow_blank=True, allow_null=True)
    email = serializers.EmailField(max_length=200,
                                   allow_blank=True, allow_null=True)
    domain = serializers.CharField(max_length=200, allow_blank=True,
                                   allow_null=True)
    domain_name = serializers.CharField(max_length=200, allow_blank=True,
                                        allow_null=True)
    domain_description = serializers.CharField(max_length=2000,
                                               allow_blank=True,
                                               allow_null=True)
    # 认证
    certified = serializers.BooleanField(default=False)
    # 审核
    approved = serializers.BooleanField(default=False)

    register_no = serializers.CharField(max_length=50,
                                        allow_blank=True, allow_null=True)
    cert_no = serializers.CharField(max_length=50,
                                    allow_blank=True, allow_null=True)
    bank_no = serializers.CharField(max_length=50,
                                    allow_blank=True, allow_null=True)
    business_license = serializers.FileField(
        allow_empty_file=True,allow_null=True)

    class Meta:
        model = CustomerAccount
        fields = (
            'id', 'no', 'source', 'username', 'password', 'role', 'active',
            'register_date', 'avatar', 'real_name', 'gender', 'birth_date',
            'phone',
            'email', 'domain', 'domain_name', 'domain_description',
            'certified', 'approved', 'register_no', 'cert_no', 'bank_no',
            'business_license')

class PendingApproveSerializer(serializers.Serializer):
    account = serializers.PrimaryKeyRelatedField(queryset=CustomerAccount.objects.all())
    # account = CustomerAccountSerializer(read_only=True)
    domain = serializers.CharField(max_length=200, allow_blank=True,
                                   allow_null=True)
    domain_name = serializers.CharField(max_length=200, allow_blank=True,
                                        allow_null=True)
    domain_description = serializers.CharField(max_length=2000,
                                               allow_blank=True,
                                               allow_null=True)
    # 认证
    certified = serializers.BooleanField(default=False)
    # 审核
    approved = serializers.BooleanField(default=False)

    register_no = serializers.CharField(max_length=50,
                                        allow_blank=True, allow_null=True)
    cert_no = serializers.CharField(max_length=50,
                                    allow_blank=True, allow_null=True)
    bank_no = serializers.CharField(max_length=50,
                                    allow_blank=True, allow_null=True)
    business_license = serializers.FileField(
        allow_empty_file=True, allow_null=True)
    create_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = PendingApprove
        fields = (
            'id', 'account','customer_account', 'domain', 'domain_name', 'domain_description',
            'certified', 'approved', 'register_no', 'cert_no', 'bank_no',
            'business_license', 'create_date')

    def create(self, validated_data):
        pending_approve = PendingApprove.objects.create(**validated_data)
        return pending_approve

class ApproveLogSerializer(serializers.Serializer):
    account = serializers.PrimaryKeyRelatedField(queryset=CustomerAccount.objects.all())
    approve_info = serializers.PrimaryKeyRelatedField(queryset=PendingApprove.objects.all())
    action_date = serializers.DateTimeField(read_only=True)
    action_type = serializers.ChoiceField(choices=ApproveLog.TYPE_CHOICES,
                                      default=ApproveLog.TYPE_CERTIFY)
    approved = serializers.BooleanField(default=False)
    message = serializers.CharField(max_length=2000, allow_null=True, allow_blank=True)
    action_user = serializers.CharField(max_length=200, allow_null=True, allow_blank=True)

    class Meta:
        model = ApproveLog
        fields = (
            'id', 'account', 'approve_info', 'action_date', 'action_type',
            'approved', 'message', 'action_user')

    def create(self, validated_data):
        approve_log = ApproveLog.objects.create(**validated_data)
        return approve_log