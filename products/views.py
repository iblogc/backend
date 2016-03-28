# -*- encoding: utf-8 -*-
try:
    import simplejson as json
except:
    import json
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from .models import Product, ProductCategory, ProductBrand, ProductBrandSeries, ProductModel
from customers.models import Company
from accounts.authorize import AccountLoginMixin
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Q
from product_utils import *
from gezbackend.utils import *
# Create your views here.

class Pdt(LoginRequiredMixin, AccountLoginMixin, ListView):

    template_name = "products/_product.html"

    def get_category(self):
        res = []
        if cache.get('category'):
            res = cache.get('category')
        else:
            for c1 in ProductCategory.objects.prefetch_related('sub_categories','sub_categories__sub_categories').filter(status=1, step=1).all():
                c1_dict = {
                    "id": c1.id,
                    "name": c1.name,
                    "second": []
                }
                res.append(c1_dict)
                for c2 in c1.sub_categories.all():
                    c2_dict = {
                        "id": c2.id,
                        "name": c2.name,
                        "third": []
                    }
                    c1_dict['second'].append(c2_dict)
                    for c3 in c2.sub_categories.all():
                        c3_dict = {
                            "id": c3.id,
                            "name": c3.name
                        }
                        c2_dict['third'].append(c3_dict)
            cache.set('category',res)

        return res

    def is_category(self, c):
        if c is None:
            return
        c = c.split(',')
        c1 = c[0]
        c2 = c[1]
        c3 = c[2]
        if c1 and c2 and c3:
            return [c3]
        if c1 and c2 and not c3:
            res = []
            for elem in ProductCategory.objects.filter(parent_id=c2).all():
                res.append(elem.id)
            return res
        if c1 and not c2 and not c3:
            res = []
            for elem_1 in ProductCategory.objects.filter(parent_id=c1).all():
                for elem in ProductCategory.objects.filter(parent_id=elem_1.id).all():
                    res.append(elem.id)
            return res
        return []

    def get_queryset(self):

        print 'c: ', self.c, 'bs: ', self.bs, 'ct: ', self.ct, 'ut: ', self.ut, 'kw: ', self.kw

        self.url = 'c=%s&bs=%s&ct=%s&ut=%s&kw=%s' % (self.c if self.c else ',,', self.bs if self.bs else ',', self.ct \
                                        if self.ct else ',', self.ut if self.ut else ',', self.kw if self.kw else '')
        self.brand_series = []
        for brand in ProductBrand.objects.filter(status=1).all():
            brand_id = brand.id
            brand = {"id": brand_id, "brand": brand.name}
            series = []
            for serie in ProductBrandSeries.objects.filter(status=1, brand_id=brand_id).all():
                series.append({"id": serie.id, "name": serie.name, "brand_id": serie.brand_id})
            brand['series'] = series
            self.brand_series.append(brand)

        self.categorys = self.get_category()
        select_q = Q(status=1)
        # sql = 'select * from gez_product where status=1 '
        #category
        cate = self.is_category(self.c)
        cate_q = Q()
        if cate:
            # sql += 'and category in%s ' % str(map(int, cate)).replace('[', '(').replace(']', ')')
            cate_q = Q(category__in=map(int, cate))

        #brand series
        bs_q = Q()
        if self.bs:
            b, s = self.bs.split(',')
            if b and not s:
                # sql += 'and brand=%s ' % b
                bs_q = Q(brand=b)
            elif b and s:
                # sql += 'and brand=%s and series=%s ' % (b, s)
                bs_q = Q(brand=b,series=s)

        #create time
        ct_q = Q()
        if self.ct:
            ct1, ct2 = self.ct.split(',')
            ct1 = get_time_stamp_min(ct1) if ct1 else 0
            ct2 = get_time_stamp_max(ct2) if ct2 else 0
            ct1 = TIME_MIN if ct1 < TIME_MIN or not ct1 else ct1
            ct2 = TIME_MAX if ct2 > TIME_MAX or not ct2 else ct2

            # sql += 'and create_time > %s and create_time < %s ' % (ct1, ct2)
            ct_q = Q(create_time__gt=ct1,create_time__lt=ct2)
        #update time
        ut_q = Q()
        if self.ut:
            ut1, ut2 = self.ut.split(',')
            ut1 = get_time_stamp_min(ut1) if ut1 else 0
            ut2 = get_time_stamp_max(ut2) if ut2 else 0
            ut1 = TIME_MIN if ut1 < TIME_MIN or not ut1 else ut1
            ut2 = TIME_MAX if ut2 > TIME_MAX or not ut2 else ut2

            # sql += 'and update_time > %s and update_time < %s' % (ut1, ut2)
            ut_q = Q(update_time__gt=ut1,update_time__lt=ut2)
        # print sql
        products = Product.objects.filter(select_q,cate_q,bs_q,ct_q,ut_q).order_by('-id')
        self.products = []

        per_page = 5

        try:
            p = Paginator(products, per_page)
            self.page = p.page(self.page_id)
            self.pages = p.num_pages
            try:
                self.next_page = Paginator(products, per_page).page(self.page_id+1).has_next()
            except:
                self.next_page = False
            for product in self.page.object_list:
                brand_name = ProductBrand.objects.get(id=product.brand, status=1).name
                series_name = ProductBrandSeries.objects.get(id=product.series, status=1).name
                company_name = Company.objects.get(id=product.company_id, status=1).name
                cname = get_category(product.category)
                # cate_obj = ProductCategory.objects.get(id=product.category)
                style = '' # ProductCategoryAttribute.objects.get(status=1, category_id=cate_obj, name=u'所属风格').value
                ctime = get_time(product.create_time)
                utime = get_time(product.update_time)
                m = ProductModel.objects.filter(status=1, product_id=product.id).all()
                charlet = ""
                if m:
                    charlet = m[0].chartlet_path

                self.products.append({
                    "id": product.id if not self.kw else change_style(str(product.id), self.kw.strip()),
                    "name": product.name if not self.kw else change_style(product.name, self.kw.strip()),
                    "product_no": product.product_no if not self.kw else change_style(product.product_no, self.kw.strip()),
                    "brand": brand_name if not self.kw else change_style(brand_name, self.kw.strip()),
                    "series": series_name if not self.kw else change_style(series_name, self.kw.strip()),
                    "cname": cname if not self.kw else change_style(cname, self.kw.strip()),
                    "company": company_name if not self.kw else change_style(company_name, self.kw.strip()),
                    "style": style if not self.kw else change_style(style, self.kw.strip()),
                    "create_time": ctime if not self.kw else change_style(ctime, self.kw.strip()),
                    "update_time": utime if not self.kw else change_style(utime, self.kw.strip()),
                    "charlet": charlet
                })
                # self.products.reverse()
        except Exception as e:
            print e.message
            self.page = 0
            self.pages = 0
            self.next_page = False

    def get_context_data(self, **kwargs):
        context = super(Pdt, self).get_context_data(**kwargs)
        context['products'] = self.products
        context['cur_page'] = self.page_id
        context['total_page'] = self.pages
        context['next'] = self.next_page
        context['url'] = self.url
        context['urls'] = json.dumps(self.url)
        context["brand_series"] = json.dumps(self.brand_series)
        context["category"] = json.dumps(self.categorys)
        return context

    def get(self, request, *args, **kwargs):
        self.page_id = int(request.GET.get('page_id', 1))
        self.c = request.GET.get('c', None)
        self.bs = request.GET.get('bs', None)
        self.ct = request.GET.get('ct', None)
        self.ut = request.GET.get('ut', None)
        self.kw = request.GET.get('kw', None)
        return super(Pdt, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return resp(0, "action success", "")