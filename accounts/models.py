# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .manager import UserManager


# Create your models here.
# 系统帐户数据表
class Account(models.Model):
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'username'
    username = models.CharField(unique=True, max_length=100, default='',
                                null=False)
    email = models.EmailField(max_length=100, default='', null=False)
    security = models.CharField(max_length=50, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)

    objects = UserManager()

# 帐户日志管理表
class AccountLog(models.Model):
    account_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='logs', default=None,
                                   null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=100, default='', null=False)
    url = models.CharField(max_length=1000, default='', null=False)
    request = models.TextField()
    response = models.TextField()
    ip_address = models.CharField(max_length=100, default='', null=False)
    create_time = models.IntegerField(default=0, null=False)


# Create your models here.
# 管理帐户数据表
class AccountAdmin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='admin', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    role = models.ForeignKey('AccountAdminRole', related_name='admin', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    work_id = models.CharField(max_length=20, default='', null=False)
    realname = models.CharField(max_length=100, default='', null=False)
    department = models.CharField(max_length=100, default='', null=False)
    status = models.IntegerField(default=1, null=False)

# 管理员角色数据表
class AccountAdminRole(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    description = models.CharField(max_length=300, default='', null=False)
    permission = models.CharField(max_length=1000, default='', null=False)
    status = models.IntegerField(default=1, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)

# 管理员部门表
class AccountAdminDepartment(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    description = models.CharField(max_length=300, default='', null=False)
    status = models.IntegerField(default=1, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)