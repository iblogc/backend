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
    CategoryCompany, CategoryBrand, CompanyBrand, ProductModelFiles, \
    ProductModelPreviews
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
        self.type = int(request.GET.get('type', 0))
        if self.type == 0:
            self.template_name = "products/_product.html"
        else:
            self.template_name = "products/_model.html"
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
        self.url = 'type=%s&kw=%s&pn=%s&c1=%s&c2=%s&c3=%s&c=%s&b=%s&s=%s&df=%s&dt=%s&order=%s&desc=%s' % (
            self.type,
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
                brand__name__icontains=self.kw) | Q(
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
        select_q = Q(type=self.type, active=1)

        products = Product.objects.select_related('brand', 'series',
                                                  'company',
                                                  'category',
                                                  'category__parent_category',
                                                  'category__parent_category__parent_category').filter(
            kw_q, com_q, b_q, pn_q, categroy_q, s_q,
            ct_q, select_q).order_by(
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
                '%scategory__parent_category__parent_category__name' % (
                    self.desc == 0 and '-' or ''))
        elif self.order == 'c2':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productcategory`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (self.desc == 0 and '-' or ''))
        elif self.order == 'c3':
            products = products.order_by(
                '%scategory__parent_category__name' % (
                    self.desc == 0 and '-' or ''))
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
            products = products.order_by(
                '%screate_time' % (self.desc == 0 and '-' or ''))
        # print order_key

        self.products = []

        per_page = 15

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
                brand_name = product.brand and product.brand.name or 'N/A'
                series_name = product.series and product.series.name or 'N/A'
                company_name = product.company and product.company.name or 'N/A'
                c1 = 'N/A'
                c2 = 'N/A'
                c3 = 'N/A'
                if product.category:
                    c3 = product.category.name
                    if product.category.parent_category:
                        c2 = product.category.parent_category.name
                        if product.category.parent_category.parent_category:
                            c1 = product.category.parent_category.parent_category.name
                # cate_obj = ProductCategory.objects.get(id=product.category)
                style = 'N/A'  # ProductCategoryAttribute.objects.get(status=1, category_id=cate_obj, name=u'所属风格').value
                ctime = get_time(product.create_time)
                utime = get_time(product.update_time)
                charlet = ""
                charlet = product.chartlet_path
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
                    "status": product.status,
                    "status_string": product.status and '启用' or '禁用',
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


def upload_product_file(request):
    product_id = request.POST.get('product_id')
    files = request.FILES.getlist('file')
    if len(files) > 0:
        file_name = files[0].name
        model_file = ProductModelFiles()
        model_file.name = file_name
        model_file.file.save(file_name, files[0])
        model_file.product_id = product_id
        model_file.save()
    return HttpResponse(json.dumps(
        {"success": 1, "id": model_file.id, "name": model_file.name,
         "url": model_file.file.url}))


def upload_product_preview(request):
    product_id = request.POST.get('product_id')
    files = request.FILES.getlist('file')
    if len(files) > 0:
        file_name = files[0].name
        model_preview = ProductModelPreviews()
        model_preview.name = file_name
        model_preview.file.save(file_name, files[0])
        model_preview.product_id = product_id
        model_preview.save()
    return HttpResponse(json.dumps(
        {"success": 1, "id": model_preview.id, "name": model_preview.name,
         "url": model_preview.file.url}))


class CategoryView(LoginRequiredMixin, TemplateView):
    template_name = "products/_category.html"

    def get(self, request, *args, **kwargs):
        self.categories = get_categories()
        return super(CategoryView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


def import_xls(request):
    if request.method == 'GET':
        return render(request, 'products/upload.html')
    else:
        cache.set('category', [])
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
        datas_array = {}
        category_array = []
        company_array = []
        brand_array = []
        series_array = []
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
                if not datas_array.get(first_category):
                    datas_array[first_category] = {}
                if not first_category in category_array:
                    category_array.append(first_category)
                if not datas_array[first_category].get(second_category):
                    datas_array[first_category][second_category] = {}
                if not second_category in category_array:
                    category_array.append(second_category)
                if not datas_array[first_category][second_category].get(
                        third_category):
                    datas_array[first_category][second_category][
                        third_category] = []
                if not third_category in category_array:
                    category_array.append(third_category)
                if not (company_name, brand_name, series_name) in \
                        datas_array[first_category][second_category][
                            third_category]:
                    datas_array[first_category][second_category][
                        third_category].append(
                        (company_name, brand_name, series_name))
                if not company_name in company_array:
                    company_array.append(company_name)
                if not brand_name in brand_array:
                    brand_array.append(brand_name)
                if not series_name in series_array:
                    series_array.append(series_name)

        max_first_category_no = 1
        max_second_category_no = 1
        max_third_category_no = 1
        max_company_no = 1
        max_brand_no = 1
        max_series_no = 1
        if ProductCategory.objects.filter(step=1).exists():
            max_first_category_no = \
                ProductCategory.objects.filter(step=1).order_by('-no')[
                    0].no + 1
        if ProductCategory.objects.filter(step=2).exists():
            max_second_category_no = \
                ProductCategory.objects.filter(step=2).order_by('-no')[
                    0].no + 1
        if ProductCategory.objects.filter(step=3).exists():
            max_third_category_no = \
                ProductCategory.objects.filter(step=3).order_by('-no')[
                    0].no + 1
        if Company.objects.exists():
            max_company_no = Company.objects.all().order_by('-no')[0].no + 1
        if ProductBrand.objects.exists():
            max_brand_no = ProductBrand.objects.all().order_by('-no')[
                               0].no + 1
        if ProductBrandSeries.objects.exists():
            max_series_no = \
                ProductBrandSeries.objects.all().order_by('-no')[0].no + 1
        exists_catecories = ProductCategory.objects.filter(name__in=category_array)
        exists_companies = Company.objects.filter(name__in=company_array)
        exists_brands = ProductBrand.objects.filter(name__in=brand_array)
        exists_series = ProductBrandSeries.objects.filter(name__in=series_array)
        first_categories = {}
        second_categories = {}
        third_categories = {}
        companies = {}
        brands = {}
        series = {}
        for category in exists_catecories:
            if category.step == 1:
                first_categories[category.name] = category
            elif category.step == 2:
                second_categories[category.name] = category
            else:
                third_categories[category.name] = category
        for company in exists_companies:
            companies[company.name] = company
        for brand in exists_brands:
            brands[brand.name] = brand
        for se in exists_series:
            series[se.name] = se
        new_first_categories = []
        new_second_categories = []
        new_third_categories = []
        new_companies = []
        new_brands = []
        new_series = []
        for first_category_name in datas_array.keys():
            if not first_categories.get(first_category_name):
                first_category = ProductCategory(
                name=first_category_name, no=max_first_category_no, step=1)
                new_first_categories.append(first_category)
                max_first_category_no += 1
        ProductCategory.objects.bulk_create(new_first_categories)
        for first_category in ProductCategory.objects.filter(name__in=[category.name for category in new_first_categories],step=1):
            first_categories[first_category.name] = first_category
        for first_category_name in datas_array.keys():
            first_category = first_categories[first_category_name]
            for second_category_name in datas_array[first_category_name].keys():
                if not second_categories.get(second_category_name):
                    second_category = ProductCategory(parent_category=first_category,
                        name=second_category_name, no=max_second_category_no, step=2)
                    new_second_categories.append(second_category)
                    max_second_category_no += 1
        ProductCategory.objects.bulk_create(new_second_categories)
        for second_category in ProductCategory.objects.filter(name__in=[category.name for category in new_second_categories],step=2):
            print second_category.id
            second_categories[second_category.name] = second_category
        for first_category_name in datas_array.keys():
            for second_category_name in datas_array[first_category_name].keys():
                second_category = second_categories[second_category_name]
                for third_category_name in datas_array[first_category_name][second_category_name].keys():
                    if not third_categories.get(third_category_name):
                        third_category = ProductCategory(
                            parent_category=second_category,
                            name=third_category_name,
                            no=max_third_category_no, step=3)
                        new_third_categories.append(third_category)
                        max_third_category_no += 1
        ProductCategory.objects.bulk_create(new_third_categories)
        for third_category in ProductCategory.objects.filter(name__in=[category.name for category in new_third_categories],step=3):
            third_categories[third_category.name] = third_category
        for first_category_name in datas_array.keys():
            for second_category_name in datas_array[first_category_name].keys():
                for third_category_name in datas_array[first_category_name][
                    second_category_name].keys():
                    for company_name,brand_name,series_name in datas_array[first_category_name][
                        second_category_name][third_category_name]:
                        print company_name,brand_name,series_name
                        if not companies.get(company_name):
                            company = Company(name=company_name,no=max_company_no)
                            max_company_no += 1
                            new_companies.append(company)
                        if not brands.get(brand_name):
                            brand = ProductBrand(name=brand_name,no=max_brand_no)
                            max_brand_no += 1
                            new_brands.append(brand)

        Company.objects.bulk_create(new_companies)
        ProductBrand.objects.bulk_create(new_brands)

        for company in Company.objects.filter(name__in=[company.name for company in new_companies]):
            companies[company.name] = company
        for brand in ProductBrand.objects.filter(name__in=[brand.name for brand in new_brands]):
            brands[brand.name] = brand
        exists_category_companies = CategoryCompany.objects.filter(category__in=third_categories.values(),company__in=companies.values())
        exists_category_brands = CategoryBrand.objects.filter(category__in=third_categories.values(),brand__in=brands.values())
        exists_company_brands = CompanyBrand.objects.filter(company__in=companies.values(),brand__in=brands.values())
        category_companies = {}
        category_brands = {}
        company_brands = {}
        for category_company in exists_category_companies:
            category_companies[(category_company.category.name,category_company.company.name)] = category_company

        for category_brand in exists_category_brands:
            category_brands[(category_brand.category.name,category_brand.brand.name)] = category_company
        for company_brand in exists_company_brands:
            company_brands[(company_brand.company.name,company_brand.brand.name)] = company_brand
        new_category_companies = []
        new_category_brands = []
        new_company_brands = []
        for first_category_name in datas_array.keys():
            for second_category_name in datas_array[first_category_name].keys():
                for third_category_name in datas_array[first_category_name][
                    second_category_name].keys():
                    category = third_categories[third_category_name]
                    for company_name, brand_name, series_name in \
                    datas_array[first_category_name][
                        second_category_name][third_category_name]:
                        company = companies[company_name]
                        if not category_companies.get((third_category_name,company_name)):
                            category_company = CategoryCompany(category=category,company=company)
                            new_category_companies.append(category_company)
        for first_category_name in datas_array.keys():
            for second_category_name in datas_array[first_category_name].keys():
                for third_category_name in datas_array[first_category_name][
                    second_category_name].keys():
                    category = third_categories[third_category_name]
                    for company_name, brand_name, series_name in \
                            datas_array[first_category_name][
                                second_category_name][third_category_name]:
                        brand = brands[brand_name]
                        if not category_brands.get((third_category_name,
                                                      brand_name)):
                            category_brand = CategoryBrand(
                                category=category, brand=brand)
                            new_category_brands.append(category_brand)
        for first_category_name in datas_array.keys():
            for second_category_name in datas_array[first_category_name].keys():
                for third_category_name in datas_array[first_category_name][
                    second_category_name].keys():
                    for company_name, brand_name, series_name in \
                            datas_array[first_category_name][
                                second_category_name][third_category_name]:
                        company = companies[company_name]
                        brand = brands[brand_name]
                        if not company_brands.get((company_name,
                                                   brand_name)):
                            company_brand = CompanyBrand(
                                company=company, brand=brand)
                            new_company_brands.append(company_brand)
        CategoryCompany.objects.bulk_create(new_category_companies)
        CategoryBrand.objects.bulk_create(new_category_brands)
        CompanyBrand.objects.bulk_create(new_company_brands)
        for first_category_name in datas_array.keys():
            for second_category_name in datas_array[first_category_name].keys():
                for third_category_name in datas_array[first_category_name][
                    second_category_name].keys():
                    for company_name, brand_name, series_name in \
                            datas_array[first_category_name][
                                second_category_name][third_category_name]:
                        brand = brands[brand_name]
                        if not series.get(series_name):
                            se = ProductBrandSeries(name=series_name,brand=brand,
                                                    no=max_series_no)
                            max_series_no += 1
                            new_series.append(se)
        ProductBrandSeries.objects.bulk_create(new_series)
        return HttpResponse(json.dumps({'success': 1}))
        # return render(request, 'products/upload.html')


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
            sheet.merge_range(first_row, 0, row_no - 1, 0, category.name,
                              format)

            # construct response

    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response[
        'Content-Disposition'] = u"attachment; filename='s%s.xlsx'" % datetime.datetime.now().microsecond

    return response


def category_attributes(request, category_id):
    attributes = get_category_attributes(category_id)
    return HttpResponse(
        json.dumps(attributes))


def category_attribute_create(request, category_id):
    name = request.POST.get('name')
    value = [v.strip() for v in request.POST.get('value').split('\n')]
    if '' in value:
        value.remove('')
    searchable = int(request.POST.get('searchable', 1)) == 1
    attribute = ProductCategoryAttribute()
    attribute.name = name
    attribute.category = ProductCategory.objects.get(pk=category_id)
    attribute.value = json.dumps(value)
    attribute.searchable = searchable
    attribute.save()
    return HttpResponse(
        json.dumps({'success': 1}))


def category_attribute_delete(request, attribute_id):
    ProductCategoryAttribute.objects.filter(pk=attribute_id).update(
        active=False)
    return HttpResponse(
        json.dumps({'success': 1}))


def category_attribute_default_values(request, attribute_id):
    values = ProductCategoryAttribute.objects.get(pk=attribute_id).value
    return HttpResponse(values)


def category_attribute_values(request, category_id, series_id):
    attributes = get_category_attribute_values(category_id, series_id)
    return HttpResponse(
        json.dumps(attributes))


def category_attribute_value_update(request, series_id):
    attribute_ids = request.POST.getlist('ids[]')
    attribute_values = request.POST.getlist('values[]')
    attribute_searchable = request.POST.getlist('searchables[]')
    if not len(attribute_ids) == len(attribute_values) == len(
            attribute_searchable):
        return HttpResponse(
            json.dumps({'success': 0}))
    for index in range(len(attribute_ids)):
        id = attribute_ids[index]
        value = attribute_values[index]
        searchable = int(attribute_searchable[index])
        attribute_value, flag = ProductCategoryAttributeValue.objects.get_or_create(
            attribute_id=id, series_id=series_id)
        attribute_value.value = value
        attribute_value.searchable = searchable == 1
        attribute_value.save()
    return HttpResponse(
        json.dumps({'success': 1}))


def category_attribute_default_value_update(request, attribute_id):
    attribute = ProductCategoryAttribute.objects.get(pk=attribute_id)
    index = int(request.POST.get('index', 0))
    text = request.POST.get('text').strip()
    values = json.loads(attribute.value)
    pre_text = ''
    if len(values) <= index:
        values.append(text)
    else:
        pre_text = values[index]
        values[index] = text
    attribute.value = json.dumps(values)
    attribute.save()
    attribute.values.filter(value=pre_text).update(value=text)
    return HttpResponse(
        json.dumps({'success': 1}))


def category_attribute_default_value_delete(request, attribute_id):
    attribute = ProductCategoryAttribute.objects.get(pk=attribute_id)
    index = int(request.POST.get('index', 0))
    values = json.loads(attribute.value)
    if index < len(values):
        pre_text = values[index]
        values.remove(pre_text)
        attribute.value = json.dumps(values)
        attribute.save()
        attribute.values.filter(value=pre_text).delete()
    return HttpResponse(
        json.dumps({'success': 1}))


def category_attribute_value_delete(request, attribute_id):
    ProductCategoryAttributeValue.objects.filter(attribute=attribute_id).update(
        active=False)
    ProductCategoryAttribute.objects.filter(pk=attribute_id).update(
        active=False)
    return HttpResponse(
        json.dumps({'success': 1}))
