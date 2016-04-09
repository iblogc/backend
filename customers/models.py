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

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.company_no)

    @property
    def company_no(self):
        return 'd%s' % self.no
