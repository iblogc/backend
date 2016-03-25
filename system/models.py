# -*- encoding:utf-8 -*-
from django.db import models

# Create your models here.

# 公共字典数据表
class Dictionary(models.Model):
    type = models.CharField(max_length=20, default='', null=False)
    code = models.CharField(max_length=20, default='', null=False)
    name = models.CharField(max_length=100, default='', null=False)
    value = models.CharField(max_length=2000, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)

# 地区数据表
class Region(models.Model):
    parent_id = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=50, default='', null=False)
    sort_id = models.IntegerField(default=0, null=False)
    level = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 菜单功能表
class Menu(models.Model):
    parent_menu = models.ForeignKey('Menu', related_name='sub_menus', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, default='', null=False)
    keycode = models.CharField(max_length=50, default='', null=False)
    url = models.CharField(max_length=300, default='', null=False)
    params = models.CharField(max_length=300, default='', null=False)
    is_menu = models.IntegerField(default=0, null=False)
    sort_id = models.IntegerField(default=0, null=False)
    icon_class = models.CharField(max_length=100, default='', null=False)
    style_css = models.CharField(max_length=300, default='', null=False)
    status = models.IntegerField(default=1, null=False)
    level = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)
