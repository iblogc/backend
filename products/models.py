# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
# Create your models here.

# 产品数据表
class Product(models.Model):
    TYPE_PRODUCT = 0
    TYPE_MODEL = 1
    TYPE_CHOICES = (
        (TYPE_PRODUCT,'产品'),
        (TYPE_MODEL,'模型'),
    )
    client_product_id = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=200, default='', null=False)
    category = models.ForeignKey('ProductCategory', related_name='products', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('ProductBrand', related_name='products', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    series = models.ForeignKey('ProductBrandSeries', related_name='products', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    product_no = models.CharField(max_length=200, default='', null=False)
    attr_val = models.CharField(max_length=100, default='', null=False)
    rule_val = models.CharField(max_length=100, default='', null=False)
    is_ornament = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=0, null=False)
    company = models.ForeignKey('customers.Company', related_name='products', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)
    args = models.TextField(default='')
    remark = models.TextField(default='')
    type = models.IntegerField(default=TYPE_PRODUCT,choices=TYPE_CHOICES)
    version_no = models.CharField(max_length=200, default='')
    norms_no = models.CharField(max_length=200, default='', null=False)
    material = models.CharField(max_length=100, default='', null=False)
    length = models.DecimalField(decimal_places=2,max_digits=10)
    width = models.DecimalField(decimal_places=2, max_digits=10)
    height = models.DecimalField(decimal_places=2, max_digits=10)
    technics = models.CharField(max_length=100, default='', null=False)
    color = models.CharField(max_length=10, default='', null=False)

    @property
    def chartlet_path(self):
        path = ''
        if self.previews.exists():
            path = self.previews.all()[0].file.url
        return path


class ProductModelFiles(models.Model):
    name = models.CharField(max_length=200, default='', null=False)
    product = models.ForeignKey("Product", related_name='files', default=None,
                              null=True, blank=True,
                              on_delete=models.SET_NULL)
    file = models.FileField(upload_to = 'file/')


class ProductModelPreviews(models.Model):
    name = models.CharField(max_length=200, default='', null=False)
    product = models.ForeignKey("Product", related_name='previews',
                              default=None,
                              null=True, blank=True,
                              on_delete=models.SET_NULL)
    file = models.FileField(upload_to = 'preview/')


# 产品分类数据表
class ProductCategory(models.Model):
    parent_category = models.ForeignKey('ProductCategory', related_name='sub_categories', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, default='', null=False)
    step = models.IntegerField(default=1, null=False)   #分类目录树所处等级
    no = models.IntegerField(default=0, null=False)
    companies = models.ManyToManyField("customers.Company", through='CategoryCompany',related_name='categories')
    brands = models.ManyToManyField('ProductBrand', through='CategoryBrand',related_name='categories')

    def __unicode__(self):
        return '%s, %s' % (self.name,self.id)

    @property
    def category_no(self):
        if self.step == 1:
            return 'a%s' % self.no
        elif self.step == 2:
            return 'b%s' % self.no
        else:
            return 'c%s' ^ self.no


class CategoryCompany(models.Model):
    category = models.ForeignKey('ProductCategory')
    company = models.ForeignKey('customers.Company')

class CategoryBrand(models.Model):
    category = models.ForeignKey('ProductCategory')
    brand = models.ForeignKey('ProductBrand')

class CompanyBrand(models.Model):
    company = models.ForeignKey('customers.Company')
    brand = models.ForeignKey('ProductBrand')

# 产品分类属性关系数据表
class ProductCategoryAttribute(models.Model):
    category = models.ForeignKey("ProductCategory", related_name='attributes', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, default='', null=False)
    value = models.TextField()
    searchable = models.BooleanField(default=True)

# 产品分类属性数值信息表
class ProductCategoryAttributeValue(models.Model):
    attribute = models.ForeignKey("ProductCategoryAttribute", related_name='values', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    series = models.ForeignKey("ProductBrandSeries", related_name='attribute_values', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    value = models.CharField(max_length=100, default='', null=False)
    searchable = models.BooleanField(default=True)

# 产品品牌关系数据
class ProductBrand(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    no = models.IntegerField(default=0, null=False)

    @property
    def brand_no(self):
        return 'e%s' % self.no


# 产品品牌与系列关系数据表
class ProductBrandSeries(models.Model):
    brand = models.ForeignKey("ProductBrand", related_name='series', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, default='', null=False)
    no = models.IntegerField(default=0, null=False)

    @property
    def series_no(self):
        return 'f%s' % self.no
