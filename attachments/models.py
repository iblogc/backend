# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
# Create your models here.
# 系统附件数据管理表
class Attachment(models.Model):
    name = models.CharField(max_length=200, default='', null=False)
    file_name = models.CharField(max_length=200, default='', null=False)
    extension = models.CharField(max_length=10, default='', null=False)
    size = models.CharField(max_length=10, default='', null=False)
    path = models.CharField(max_length=300, default='', null=False)
    width = models.FloatField(default=0, null=False)
    height = models.FloatField(default=0, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='attachments', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    create_time = models.IntegerField(default=0, null=False)

