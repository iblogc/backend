# -*- encoding:utf-8 -*-
from django.db import models

# Create your models here.
# 楼盘数据表
class Property(models.Model):
    name = models.CharField(max_length=200, default='', null=False, db_index=True)
    alias_name = models.CharField(max_length=200, default='', null=False)
    sale_name = models.CharField(max_length=300, default='', null=False)
    brand = models.CharField(max_length=200, default='', null=False)
    key_code = models.CharField(max_length=50, default='', null=False)
    approve_code = models.CharField(max_length=100, default='', null=False)
    province = models.CharField(max_length=200, default='', null=False)
    address = models.CharField(max_length=200, default='', null=False)
    longitude = models.FloatField(default=0, null=False)
    latitude = models.FloatField(default=0, null=False)
    thumb = models.CharField(max_length=200, default='', null=False)
    plan_area = models.CharField(max_length=200, default='', null=False)
    build_area = models.CharField(max_length=200, default='', null=False)
    plan_house = models.CharField(max_length=200, default='', null=False)
    green_rate = models.CharField(max_length=200, default='', null=False)
    cubage_rate = models.CharField(max_length=200, default='', null=False)
    house = models.CharField(max_length=200, default='', null=False)
    build_type = models.CharField(max_length=500, default='', null=False)
    acreage = models.CharField(max_length=500, default='', null=False)
    aspect = models.CharField(max_length=100, default='', null=False)
    min_price = models.FloatField(default=0, null=False)
    max_price = models.FloatField(default=0, null=False)
    min_avg_price = models.FloatField(default=0, null=False)
    max_avg_price = models.FloatField(default=0, null=False)
    property_age_limit = models.CharField(max_length=200, default='', null=False)
    property_type = models.CharField(max_length=200, default='', null=False)
    renovation = models.CharField(max_length=200, default='', null=False)
    traffic = models.TextField()
    education = models.TextField()
    life = models.TextField()
    environment = models.TextField()
    property_manufactor = models.CharField(max_length=200, default='', null=False)
    develop_manufactor = models.CharField(max_length=200, default='', null=False)
    build_date = models.IntegerField(default=0, null=False)
    complete_date = models.IntegerField(default=0, null=False)
    deliver_date = models.IntegerField(default=0, null=False)
    persell = models.CharField(max_length=200, default='', null=False)
    tags = models.CharField(max_length=300, default='', null=False)
    account_id = models.IntegerField(default=0, null=False)
    license = models.CharField(max_length=200, default='', null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 楼盘详细信息数据表
class PropertyProfile(models.Model):
    property = models.ForeignKey("Property", related_name='profiles', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=20, default='', null=False)
    profile_data = models.TextField()
    account_id = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 楼盘户型关系数据表
class PropertyApartment(models.Model):
    property = models.ForeignKey("Property", related_name='apartments', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    build_type = models.CharField(max_length=100, default='', null=False)
    name = models.CharField(max_length=100, default='', null=False)
    description = models.CharField(max_length=300, default='', null=False)
    thumb = models.CharField(max_length=300, default='', null=False)
    acreage = models.CharField(max_length=10, default='', null=False)
    aspect = models.CharField(max_length=100, default='', null=False)
    coordinate = models.CharField(max_length=1000, default='', null=False)
    height = models.FloatField(default=0, null=False)
    sale_house = models.TextField()
    room = models.IntegerField(default=0, null=False)
    hall = models.IntegerField(default=0, null=False)
    toilet = models.IntegerField(default=0, null=False)
    kitchen = models.IntegerField(default=0, null=False)
    balcony = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 楼盘相册关系数据表
class PropertyAlbum(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    description = models.CharField(max_length=300, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 楼盘相册与照片关系数据表
class PropertyAlbumPicture(models.Model):
    album_id = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=200, default='', null=False)
    description = models.CharField(max_length=300, default='', null=False)
    thumb = models.CharField(max_length=300, default='', null=False)
    create_time = models.IntegerField(default=0, null=False)
