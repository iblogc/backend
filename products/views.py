# -*- encoding: utf-8 -*-
try:
    import simplejson as json
except:
    import json
import datetime
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from .models import Product, ProductCategory, ProductBrand, ProductBrandSeries, \
    ProductModel, CategoryCompany, CategoryBrand, CompanyBrand
from customers.models import Company
from accounts.authorize import AccountLoginMixin
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Q
from product_utils import *
from gezbackend.utils import *

import xlrd
import xlwt
from xlsxwriter.workbook import Workbook
import StringIO


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
            com_q = Q(company__name__icontains=self.com)
        b_q = Q()
        if self.b:
            b_q = Q(brand__name__icontains=self.b)
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
        return HttpResponse(json.dumps(self.product))


class CategoryView(LoginRequiredMixin, TemplateView):
    template_name = "products/_category.html"

    def get(self, request, *args, **kwargs):
        self.categories = get_categories()
        return super(CategoryView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


def sub_categories(request, category_id):
    categories = get_sub_categories(category_id)
    return HttpResponse(json.dumps(categories))


def category_create(request, category_id):
    name = request.POST.get('name').strip()
    step = request.POST.get('step').strip()
    parent_category = ProductCategory.objects.get(pk=category_id)
    max_no = 1
    if ProductCategory.objects.filter(step=step).exists():
        max_no = ProductCategory.objects.filter(step=step).order_by('-no')[0].no + 1
    category_dict = {'id': 0, 'name': name}
    category = ProductCategory()
    category.parent_category = parent_category
    category.name = name
    category.step = step
    category.status = 1
    category.no = max_no
    category.save()
    category_dict['id'] = category.id
    return HttpResponse(json.dumps(category_dict))


def category_update(request, category_id):
    name = request.POST.get('name').strip()
    ProductCategory.objects.filter(pk=category_id).update(name=name)
    return HttpResponse(json.dumps({'success': 1}))


def category_delete(request, category_id):
    parent_category = ProductCategory.objects.get(pk=category_id)
    if parent_category.sub_categories.exists():
        parent_category.sub_categories.all().delete()
    parent_category.delete()
    return HttpResponse(json.dumps({'success': 1}))


def companies(request, category_id):
    companies = get_category_companies(category_id)
    return HttpResponse(json.dumps(companies))


def company_create(request, category_id):
    name = request.POST.get('name').strip()
    category = ProductCategory.objects.get(pk=category_id)
    max_no = 1
    if Company.objects.exists():
        max_no = Company.objects.all().order_by('-no')[0].no + 1
    company_dict = {'id': 0, 'name': name}
    company, flag = Company.objects.get_or_create(name=name)
    if company.no == 0:
        company.no = max_no
        company.save()
    CategoryCompany.objects.get_or_create(category=category, company=company)
    company_dict['id'] = company.id
    return HttpResponse(json.dumps(company_dict))


def company_delete(request, category_id, company_id):
    category = ProductCategory.objects.get(pk=category_id)
    company = Company.objects.get(pk=company_id)
    CategoryCompany.objects.filter(company=company, category=category).delete()
    return HttpResponse(json.dumps({'success': 1}))


def company_update(request, company_id):
    name = request.POST.get('name').strip()
    Company.objects.filter(pk=company_id).update(name=name)
    return HttpResponse(json.dumps({'success': 1}))


def brands(request, category_id, company_id):
    brands = get_company_brands(category_id, company_id)
    return HttpResponse(json.dumps(brands))


def brand_create(request, category_id, company_id):
    name = request.POST.get('name').strip()
    category = ProductCategory.objects.get(pk=category_id)
    company = Company.objects.get(pk=company_id)
    max_no = 1
    if ProductBrand.objects.exists():
        max_no = ProductBrand.objects.all().order_by('-no')[0].no + 1
    brand_dict = {'id': 0, 'name': name}
    brand, flag = ProductBrand.objects.get_or_create(name=name)
    if brand == 0:
        brand.no = max_no
        brand.save()
    CategoryBrand.objects.get_or_create(category=category, brand=brand)
    CompanyBrand.objects.get_or_create(company=company, brand=brand)
    brand_dict['id'] = brand.id
    return HttpResponse(json.dumps(brand_dict))


def brand_delete(request, category_id, company_id, brand_id):
    category = ProductCategory.objects.get(pk=category_id)
    company = Company.objects.get(pk=company_id)
    brand = ProductBrand.objects.get(pk=brand_id)
    CompanyBrand.objects.filter(company=company, brand=brand).delete()
    if not brand.companies.exists():
        CategoryBrand.objects.filter(category=category, brand=brand).delete()
    return HttpResponse(json.dumps({'success': 1}))


def brand_update(request, brand_id):
    name = request.POST.get('name').strip()
    ProductBrand.objects.filter(pk=brand_id).update(name=name)
    return HttpResponse(json.dumps({'success': 1}))


def brand_series(request, brand_id):
    series = get_brand_series(brand_id)
    return HttpResponse(json.dumps(series))


def series_create(request, brand_id):
    name = request.POST.get('name').strip()
    brand = ProductBrand.objects.get(pk=brand_id)
    max_no = 1
    if ProductBrandSeries.objects.exists():
        max_no = ProductBrandSeries.objects.all().order_by('-no')[0].no + 1
    series_dict = {'id': 0, 'name': name}
    series = ProductBrandSeries()
    series.name = name
    series.brand = brand
    series.no = max_no
    series.save()
    series_dict['id'] = series.id
    return HttpResponse(json.dumps(series_dict))


def series_delete(request, series_id):
    ProductBrandSeries.objects.filter(pk=series_id).delete()
    return HttpResponse(json.dumps({'success': 1}))


def series_update(request, series_id):
    name = request.POST.get('name').strip()
    ProductBrandSeries.objects.filter(pk=series_id).update(name=name)
    return HttpResponse(json.dumps({'success': 1}))


def import_xls(request):
    xls_file = request.FILES.get('file')
    data = xlrd.open_workbook(file_contents=xls_file.read())
    table = data.sheets()[0]
    row_count = table.nrows
    cell_count = table.ncols
    print row_count, cell_count
    first_category = ''
    second_category = ''
    third_category = ''
    company_name = ''
    brand_name = ''
    series_name = ''
    datas_array = []
    for row_no in range(1, row_count):
        cells = table.row_values(row_no)
        if cells:
            if cells[0].strip() != '':
                first_category = cells[0].strip()
            if cells[1].strip() != '':
                second_category = cells[1].strip()
            if cells[2].strip() != '':
                third_category = cells[2].strip()
            if cells[3].strip() != '':
                company_name = cells[3].strip()
            if cells[4].strip() != '':
                brand_name = cells[4].strip()
            if cells[5].strip() != '':
                series_name = cells[5].strip()
            if first_category == '':
                continue
            datas_array.append((first_category, second_category, third_category, company_name, brand_name, series_name))
    print datas_array
    for data_dict in datas_array:
        try:
            max_first_category_no = 1
            max_second_category_no = 1
            max_third_category_no = 1
            max_company_no = 1
            max_brand_no = 1
            max_series_no = 1
            if ProductCategory.objects.filter(step=1).exists():
                max_first_category_no = ProductCategory.objects.filter(step=1).order_by('-no')[0].no + 1
            first_category, flag = ProductCategory.objects.get_or_create(name=data_dict[0], step=1)
            if first_category.no == 0:
                first_category.no = max_first_category_no
                first_category.save()
            if ProductCategory.objects.filter(step=2).exists():
                max_second_category_no = ProductCategory.objects.filter(step=2).order_by('-no')[0].no + 1
            second_category, flag = ProductCategory.objects.get_or_create(name=data_dict[1], step=2,
                                                                          parent_category=first_category)
            if second_category.no == 0:
                second_category.no = max_second_category_no
                second_category.save()
            if ProductCategory.objects.filter(step=3).exists():
                max_third_category_no = ProductCategory.objects.filter(step=3).order_by('-no')[0].no + 1
            third_category, flag = ProductCategory.objects.get_or_create(name=data_dict[2], step=3,
                                                                         parent_category=second_category)
            if third_category.no == 0:
                third_category.no = max_third_category_no
                third_category.save()
            if data_dict[3] == '':
                continue
            if Company.objects.exists():
                max_company_no = Company.objects.all().order_by('-no')[0].no + 1
            company, flag = Company.objects.get_or_create(name=data_dict[3])
            if company.no == 0:
                company.no = max_company_no
                company.save()
            if data_dict[4] == '':
                continue
            CategoryCompany.objects.get_or_create(category=third_category, company=company)
            if ProductBrand.objects.exists():
                max_brand_no = ProductBrand.objects.all().order_by('-no')[0].no + 1
            brand, flag = ProductBrand.objects.get_or_create(name=data_dict[4])
            if brand.no == 0:
                brand.no = max_brand_no
                brand.save()
            CategoryBrand.objects.get_or_create(category=third_category, brand=brand)
            CompanyBrand.objects.get_or_create(company=company, brand=brand)
            if data_dict[5] == '':
                continue
            if ProductBrandSeries.objects.exists():
                max_series_no = ProductBrandSeries.objects.all().order_by('-no')[0].no + 1
            series, flag = ProductBrandSeries.objects.get_or_create(name=data_dict[5], brand=brand)
            if series.no == 0:
                series.no = max_series_no
                series.save()
        except Exception as e:
            print e.message
    return HttpResponse(json.dumps({'success': 1}))


def export_xls(request):
    output = StringIO.StringIO()

    with Workbook(output) as book:
        format = book.add_format()
        format.set_border(1)
        format.set_align('center')
        format.set_valign('vcenter')
        sheet = book.add_worksheet('test')
        sheet.write(0, 0, u'一级分类', format)
        sheet.write(0, 1, u'二级分类', format)
        sheet.write(0, 2, u'三级分类', format)
        sheet.write(0, 3, u'厂家', format)
        sheet.write(0, 4, u'品牌', format)
        sheet.write(0, 5, u'系列', format)

        sheet.set_column(0, 0, 10)
        sheet.set_column(1, 1, 15)
        sheet.set_column(2, 2, 30)
        sheet.set_column(3, 3, 10)
        sheet.set_column(4, 4, 10)
        sheet.set_column(5, 5, 10)

        categories = ProductCategory.objects.filter(step=1)
        row_no = 1
        for category in categories:
            first_row = row_no
            for c2 in category.sub_categories.all():
                second_row = row_no
                for c3 in c2.sub_categories.all():
                    for company in c3.companies.all():
                        for brand in c3.brands.filter(companies=company):
                            for series in brand.series.all():
                                sheet.write(row_no, 2, c3.name, format)
                                sheet.write(row_no, 3, company.name, format)
                                sheet.write(row_no, 4, brand.name, format)
                                sheet.write(row_no, 5, series.name, format)
                                row_no += 1
                sheet.merge_range(second_row, 1, row_no - 1, 1, c2.name, format)
            sheet.merge_range(first_row, 0, row_no - 1, 0, category.name, format)

            # construct response

    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = u"attachment; filename='s%s.xlsx'" % datetime.datetime.now().microsecond

    return response


def category_search(request):
    kw = request.GET.get('kw').strip()
    per_page = int(request.GET.get('per_page', 50))
    page = int(request.GET.get('page', 1))
    series = ProductBrandSeries.objects.filter(
        Q(name__icontains=kw) | Q(brand__name__icontains=kw) | Q(brand__companies__name__icontains=kw) | Q(
            brand__categories__name__icontains=kw) | Q(brand__categories__parent_category__name__icontains=kw) | Q(
            brand__categories__parent_category__parent_category__name__icontains=kw))
    result = []
    for se in series:
        for c3 in se.brand.categories.all():
            for company in se.brand.companies.all():
                result.append({'first_category': c3.parent_category.parent_category.name,
                               'second_category': c3.parent_category.name, 'third_category': c3.name,
                               'company': company.name, 'brand': se.brand.name, 'series': se.name,})
    p = Paginator(result, per_page)
    current_page = p.page(page)
    total_pages = p.num_pages
    return HttpResponse(json.dumps({'data':current_page.object_list,'total_pages':total_pages,'current_page':page,'id':se.id}))
