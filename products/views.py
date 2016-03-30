# -*- encoding: utf-8 -*-
try:
    import simplejson as json
except:
    import json
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from .models import Product, ProductCategory, ProductBrand, ProductBrandSeries, \
    ProductModel
from customers.models import Company
from accounts.authorize import AccountLoginMixin
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Q
from product_utils import *
from gezbackend.utils import *


# Create your views here.

class ProductView(LoginRequiredMixin, TemplateView):
    template_name = "products/_product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['products'] = self.products
        context['cur_page'] = self.page_id
        context['total_page'] = self.pages
        context['next'] = self.next_page
        context['url'] = self.url
        context['urls'] = json.dumps(self.url)
        context["category"] = json.dumps(get_categories())
        return context

    def get(self, request, *args, **kwargs):
        self.page_id = int(request.GET.get('page_id', 1))

        self.kw = request.GET.get('kw', '')
        self.pn = request.GET.get('pn', '')
        self.c1 = int(request.GET.get('c1', 0))
        self.c2 = int(request.GET.get('c2', 0))
        self.c3 = int(request.GET.get('c3', 0))
        self.com = request.GET.get('c', '')
        self.b = request.GET.get('b', '')
        self.s = request.GET.get('s', '')
        self.order = request.GET.get('order', '')
        self.desc = int(request.GET.get('desc', '0'))
        df = request.GET.get('df', '')
        dt = request.GET.get('dt', '')
        ct1 = get_time_stamp_min(df) if df else 0
        ct2 = get_time_stamp_max(dt) if dt else 0
        self.df = min(ct1, ct2)
        self.dt = max(ct1, ct2)
        self.url = 'kw=%s&pn=%s&c1=%s&c2=%s&c3=%s&c=%s&b=%s&s=%s&df=%s&dt=%s&order=%s&desc=%s' % (
            self.kw, self.pn, self.c1, self.c2, self.c3, self.com, self.b,
            self.s,
            df, dt, self.order, self.desc)
        print self.url
        kw_q = Q()
        if self.kw:
            kw_q = Q(name__icontains=self.kw) | Q(
                product_no__icontains=self.kw) | Q(
                category__parent_category__parent_category__name__icontains=self.kw) | Q(
                category__parent_category__name__icontains=self.kw) | Q(
                category__name__icontains=self.kw) | Q(
                company__name__icontains=self.kw) | Q(
                company__alias_name__icontains=self.kw) | Q(
                brand__name__icontains=self.kw) | Q(
                brand__name_en__icontains=self.kw) | Q(
                series__name__icontains=self.kw)

        pn_q = Q()
        if self.pn:
            pn_q = Q(product_no__icontains=self.pn)
        categroy_q = Q()
        if self.c1:
            categroy_q = Q(category__parent_category__parent_category=self.c1)
            if self.c2:
                categroy_q = Q(category__parent_category=self.c2)
                if self.c3:
                    categroy_q = Q(category=self.c3)
        com_q = Q()
        if self.com:
            com_q = Q(company__name__icontains=self.com) | Q(
                company__alias_name__icontains=self.com)
        b_q = Q()
        if self.b:
            b_q = Q(brand__name__icontains=self.b) | Q(
                brand__name_en__icontains=self.b)
        s_q = Q()
        if self.s:
            s_q = Q(series__name__icontains=self.b)
        ct_q = Q()
        if ct1 or ct2:
            ct_q = Q(create_time__gt=self.df, create_time__lt=self.dt)
        select_q = Q()

        products = Product.objects.select_related('brand', 'series',
                                                  'company',
                                                  'category',
                                                  'category__parent_category',
                                                  'category__parent_category__parent_category').prefetch_related(
            'models').filter(kw_q, com_q, b_q, pn_q, categroy_q, s_q,
                             ct_q).order_by(
            '-id')
        if self.order == 'n':
            products = products.extra(select={
                'gbk_title': 'convert(`products_product`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 'pn':
            products = products.extra(select={
                'gbk_title': 'convert(`products_product`.`product_no` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 'c1':
            products = products.order_by(
                '%scategory__parent_category__parent_category__name' % (self.desc == 0 and '-' or ''))
        elif self.order == 'c2':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productcategory`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 'c3':
            products = products.order_by(
                '%scategory__parent_category__name' % (self.desc == 0 and '-' or ''))
        elif self.order == 'c':
            products = products.extra(select={
                'gbk_title': 'convert(`customers_company`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 'b':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productbrand`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 's':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productbrandseries`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 'd':
            products = products.order_by('%screate_time' % (self.desc == 0 and '-' or ''))
        # print order_key

        self.products = []

        per_page = 5

        try:
            p = Paginator(products, per_page)
            self.page = p.page(self.page_id)
            self.pages = p.num_pages
            try:
                self.next_page = Paginator(products, per_page).page(
                    self.page_id + 1).has_next()
            except:
                self.next_page = False
            for product in self.page.object_list:
                brand_name = product.brand and product.brand.name or ''
                series_name = product.series and product.series.name or ''
                company_name = product.company and product.company.name or ''
                c1 = ''
                c2 = ''
                c3 = ''
                if product.category:
                    c3 = product.category.name
                    if product.category.parent_category:
                        c2 = product.category.parent_category.name
                        if product.category.parent_category.parent_category:
                            c1 = product.category.parent_category.parent_category.name
                # cate_obj = ProductCategory.objects.get(id=product.category)
                style = ''  # ProductCategoryAttribute.objects.get(status=1, category_id=cate_obj, name=u'所属风格').value
                ctime = get_time(product.create_time)
                utime = get_time(product.update_time)
                m = product.models.all()
                charlet = ""
                if m:
                    charlet = m[0].chartlet_path
                self.products.append({
                    "id": product.id if not self.kw else change_style(
                        str(product.id), self.kw.strip()),
                    "name": product.name if not self.kw else change_style(
                        product.name, self.kw.strip()),
                    "product_no": product.product_no if not self.kw else change_style(
                        product.product_no,
                        self.kw.strip()),
                    "brand": brand_name if not self.kw else change_style(
                        brand_name, self.kw.strip()),
                    "series": series_name if not self.kw else change_style(
                        series_name, self.kw.strip()),
                    "c1": c1 if not self.kw else change_style(c1,
                                                              self.kw.strip()),
                    "c2": c2 if not self.kw else change_style(c2,
                                                              self.kw.strip()),
                    "c3": c3 if not self.kw else change_style(c3,
                                                              self.kw.strip()),
                    "company": company_name if not self.kw else change_style(
                        company_name, self.kw.strip()),
                    "style": style if not self.kw else change_style(style,
                                                                    self.kw.strip()),
                    "create_time": ctime if not self.kw else change_style(ctime,
                                                                          self.kw.strip()),
                    "update_time": utime if not self.kw else change_style(utime,
                                                                          self.kw.strip()),
                    "charlet": charlet,
                    "status": product.status and '启用' or '禁用',
                })
                # self.products.reverse()
        except Exception as e:
            print e.message
            self.page = 0
            self.pages = 0
            self.next_page = False
        return super(ProductView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return resp(0, "action success", "")


class ProductActiveView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        Product.objects.filter(pk=kwargs['pk']).update(status=1)
        return resp(0, "action success", "")


class ProductVoidView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        Product.objects.filter(pk=kwargs['pk']).update(status=0)
        return resp(0, "action success", "")


class ProductDetailView(LoginRequiredMixin, TemplateView):
    template_name = "products/_product.html"

    def post(self, request, *args, **kwargs):
        p = Product.objects.get(id=kwargs['pk'])
        self.product = {
            "id": p.id,
            "product_no": p.product_no,
            "product_name": p.name,
            "company_name": p.company.name,
            "category_name": get_category(p.category.id),
            "brand": p.brand.name,
            "series": p.series.name,
            "model": {},
            "args": {},
            "remarks": p.remark,
        }
        if p.models.exists():
            model = p.models.all()[0]
            self.product['model'] = {
                "model_id": model.id,
                "norm_no": model.norms_no,
                "version": model.version_no,
                # "model_name": model.name,
                "norms": json.loads(model.norms),
                "material": model.material,
                "color": model.color,
                'chartlet': model.chartlet_path
            }
        self.product['args'] = json.loads(p.args.decode('utf-8'))
        return HttpResponse(json.dumps(self.product))\

class CategoryView(LoginRequiredMixin, TemplateView):
    template_name = "products/_category.html"

    def get(self, request, *args, **kwargs):
        self.categories = get_categories()
        return super(CategoryView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context