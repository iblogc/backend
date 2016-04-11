# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings


# Create your models here.

class CustomerAccount(models.Model):
    SOURCE_MAIN = 0
    SOURCE_DESIGN = 1
    SOURCE_OR = 2
    SOURCE_CHOICES = (
        (0, '官网'),
        (1, '设计师平台'),
        (2, '电商平台')
    )

    ROLE_NORMAL = 0
    ROLE_DESIGNER = 1
    ROLE_SUPPLIERS = 2
    ROLE_DECORATION = 3
    ROLE_CHOICES = (
        (0, '普通用户'),
        (1, '设计师'),
        (2, '供应商'),
        (3, '装修公司')
    )

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = (
        (GENDER_MALE, '男'),
        (GENDER_FEMALE, '女'),
    )

    no = models.CharField(max_length=200, default=None, null=True, blank=True)
    #来源
    source = models.IntegerField(choices=SOURCE_CHOICES, default=SOURCE_MAIN)
    #用户名
    username = models.CharField(max_length=200, default=None, null=True,
                                blank=True)
    password = models.CharField(max_length=50, default=None, null=True,
                                blank=True)
    #角色
    role = models.IntegerField(choices=ROLE_CHOICES, default=ROLE_NORMAL)
    #状态
    active = models.BooleanField(default=True)
    #注册日期
    register_date = models.DateTimeField(default=None, null=True, blank=True)
    #头像
    avatar = models.ImageField(default=None, null=True, blank=True,
                               upload_to='avatar/')
    #真实姓名
    real_name = models.CharField(max_length=200, default=None, null=True,
                                 blank=True)
    #性别
    gender = models.IntegerField(choices=GENDER_CHOICES, default=GENDER_MALE)
    #生日
    birth_date = models.DateField(default=None, null=True, blank=True)
    #手机号码
    phone = models.CharField(max_length=50, default=None, null=True, blank=True)
    #邮箱
    email = models.EmailField(max_length=200, default=None, null=True,
                              blank=True)
    email_certified = models.BooleanField(default=False)
    # 电话有效性认证
    phone_certified = models.BooleanField(default=False)
    #域名
    domain = models.CharField(max_length=200,default=None,null=True,blank=True)
    #名称
    domain_name = models.CharField(max_length=200, default=None, null=True,
                              blank=True)
    #描述
    domain_description = models.CharField(max_length=2000, default=None, null=True,
                              blank=True)
    # 认证
    certified = models.BooleanField(default=False)
    # 审核
    approved = models.BooleanField(default=False)
    #注册号
    register_no = models.CharField(max_length=50, default=None, null=True,
                                   blank=True)
    #身份信息
    cert_no = models.CharField(max_length=50, default=None, null=True,
                               blank=True)
    #银行帐号
    bank_no = models.CharField(max_length=50, default=None, null=True,
                               blank=True)
    #营业执照
    business_license = models.FileField(default=None, null=True, blank=True,
                                        upload_to='business_license/')

    def __unicode__(self):
        return '%s: %s' % (CustomerAccount.SOURCE_CHOICES[self.source][1],self.username)

class OtherAccount(models.Model):
    """
        第三方用户表，商铺、电商的用户
    """
    platform = models.ForeignKey('CustomerAccount', related_name='other')
    platform_code = models.CharField(max_length=128, default='', null=False)
    username = models.CharField(max_length=128, default='', null=False)
    user_code = models.CharField(max_length=32, default='', null=False)

class PendingApprove(models.Model):
    account = models.ForeignKey('CustomerAccount',related_name='pending_approves')
    domain = models.CharField(max_length=200, default=None, null=True,
                              blank=True)
    domain_name = models.CharField(max_length=200, default=None, null=True,
                                   blank=True)
    domain_description = models.CharField(max_length=2000, default=None,
                                          null=True,
                                          blank=True)
    # 认证
    certified = models.BooleanField(default=False)
    # 审核
    approved = models.BooleanField(default=False)

    register_no = models.CharField(max_length=50, default=None, null=True,
                                   blank=True)
    cert_no = models.CharField(max_length=50, default=None, null=True,
                               blank=True)
    bank_no = models.CharField(max_length=50, default=None, null=True,
                               blank=True)
    business_license = models.FileField(default=None, null=True, blank=True,
                                        upload_to='business_license/')
    create_date = models.DateTimeField(auto_now=True)


class AccountKey(models.Model):
    account = models.OneToOneField('CustomerAccount', related_name='key')
    token = models.CharField(max_length=128, unique=True, default='',
                             null=False)
    license = models.CharField(max_length=64, unique=True, default='',
                               null=False)
    app_secret = models.CharField(max_length=64, unique=True, default='',
                                  null=False)


class ApproveLog(models.Model):
    TYPE_CERTIFY = 0
    TYPE_APPROVE = 1
    TYPE_CHOICES = (
        (TYPE_CERTIFY, '证明'),
        (TYPE_APPROVE, '审核')
    )

    account = models.ForeignKey('CustomerAccount', related_name='approve_logs')
    approve_info = models.OneToOneField('PendingApprove', related_name='approve_log')
    action_date = models.DateTimeField(auto_now=True)
    action_type = models.IntegerField(choices=TYPE_CHOICES,
                                      default=TYPE_CERTIFY)
    approved = models.BooleanField(default=False)
    message = models.CharField(max_length=2000, default=None, null=True,
                               blank=True)
    action_user = models.CharField(max_length=200, default=None, null=True,
                                   blank=True)
