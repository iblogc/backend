# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
# Create your models here.

# 客户单位数据表
class Company(models.Model):
    name = models.CharField(max_length=200, default='', null=False)
    no = models.IntegerField(default=0, null=False)
    brands = models.ManyToManyField('products.ProductBrand',through='products.CompanyBrand',related_name='companies')
    active = models.BooleanField(default=True)

    @property
    def company_no(self):
        return 'd%s' % self.no

# 客户单位与帐户关系绑定数据表
class CompanyExamine(models.Model):
    status = models.IntegerField(default=0, null=False)
    desciprtion = models.CharField(max_length=500, default='', null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='examine', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


class CompanyLicense(models.Model):
    app_key = models.CharField(max_length=64, default='', null=False)
    license_key = models.CharField(max_length=128, default='', null=False)
    communication = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=0, null=False)
    company = models.ForeignKey("Company", related_name='licenses', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


class CompanyAgency(models.Model):
    company_id = models.IntegerField(default=0, null=False)
    agency_company_id = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)
