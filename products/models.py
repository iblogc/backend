# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
# Create your models here.

# 产品数据表
class Product(models.Model):
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


# 产品模型关系数据表
class ProductModel(models.Model):
    product = models.ForeignKey("Product", related_name='models', default=None, null=True, blank=True,
                                on_delete=models.SET_NULL)
    version_no = models.CharField(max_length=200, default='')
    norms_no = models.CharField(max_length=200, default='', null=False)
    name = models.CharField(max_length=200, default='', null=False)
    material = models.CharField(max_length=100, default='', null=False)
    norms = models.CharField(max_length=100, default='', null=False)
    technics = models.CharField(max_length=100, default='', null=False)
    model_path = models.CharField(max_length=300, default='', null=False)
    chartlet_path = models.CharField(max_length=300, default='', null=False)
    color = models.CharField(max_length=10, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 产品商品关系数据表
class ProductCommodity(models.Model):
    product = models.ForeignKey("Product", related_name='commodities', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    model = models.CharField(max_length=500, default='', null=False)
    name = models.CharField(max_length=200, default='', null=False)
    category = models.CharField(max_length=500, default='', null=False)
    brand = models.CharField(max_length=300, default='', null=False)
    series = models.CharField(max_length=300, default='', null=False)
    model_position = models.TextField()
    account_limit = models.TextField()   # license,
    company_id = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)

# 商品货品关系数据表
class ProductCommodityGoods(models.Model):
    commodity = models.ForeignKey("ProductCommodity", related_name='goods', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, default='', null=False)
    sale_title = models.CharField(max_length=300, default='', null=False)
    category = models.CharField(max_length=500, default='', null=False)
    brand = models.CharField(max_length=300, default='', null=False)
    series = models.CharField(max_length=300, default='', null=False)
    param_search = models.TextField()
    param_full = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0, null=False)
    price_advise = models.FloatField(default=0, null=False)
    inventory = models.IntegerField(default=0, null=False)
    company_id = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


# 产品分类数据表
class ProductCategory(models.Model):
    parent_category = models.ForeignKey('ProductCategory', related_name='sub_categories', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, default='', null=False)
    step = models.IntegerField(default=1, null=False)   #分类目录树所处等级
    no = models.IntegerField(default=0, null=False)
    companies = models.ManyToManyField("customers.Company", through='CategoryCompany',related_name='categories')
    brands = models.ManyToManyField('ProductBrand', through='CategoryBrand',related_name='categories')

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
    type = models.CharField(max_length=10, default='', null=False)
    value = models.TextField()
    is_search = models.IntegerField(default=0, null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)

# 产品分类属性数值信息表
class ProductCategoryAttributeValue(models.Model):
    attribute = models.ForeignKey("ProductCategoryAttribute", related_name='values', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    parent_id = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=100, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


class ProductCategorySearch(models.Model):
    category = models.ForeignKey("ProductCategory", related_name='search', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


class ProductCategorySearchValue(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    search = models.ForeignKey("ProductCategorySearch", related_name='values', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, default='', null=False)
    status = models.IntegerField(default=0, null=False)
    create_time = models.IntegerField(default=0, null=False)
    update_time = models.IntegerField(default=0, null=False)


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
