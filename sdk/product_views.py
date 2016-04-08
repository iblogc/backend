# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory, Product
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Q

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        type = int(request.GET.get('type', 0))
        page_id = int(request.GET.get('page_id', 1))

        kw = request.GET.get('kw', '')
        pn = request.GET.get('pn', '')
        c1 = int(request.GET.get('c1', 0))
        c2 = int(request.GET.get('c2', 0))
        c3 = int(request.GET.get('c3', 0))
        com = request.GET.get('c', '')
        b = request.GET.get('b', '')
        s = request.GET.get('s', '')
        order = request.GET.get('order', '')
        desc = int(request.GET.get('desc', '0'))
        df = request.GET.get('df', '')
        dt = request.GET.get('dt', '')
        ct1 = get_time_stamp_min(df) if df else 0
        ct2 = get_time_stamp_max(dt) if dt else 0
        df = min(ct1, ct2)
        dt = max(ct1, ct2)
        url = 'type=%s&kw=%s&pn=%s&c1=%s&c2=%s&c3=%s&c=%s&b=%s&s=%s&df=%s&dt=%s&order=%s&desc=%s' % (
            type,
            kw, pn, c1, c2, c3, com, b,
            s,
            df, dt, order, desc)
        print url
        kw_q = Q()
        if kw:
            kw_q = Q(name__icontains=kw) | Q(
                product_no__icontains=kw) | Q(
                category__parent_category__parent_category__name__icontains=kw) | Q(
                category__parent_category__name__icontains=kw) | Q(
                category__name__icontains=kw) | Q(
                company__name__icontains=kw) | Q(
                brand__name__icontains=kw) | Q(
                series__name__icontains=kw)

        pn_q = Q()
        if pn:
            pn_q = Q(product_no__icontains=pn)
        categroy_q = Q()
        if c1:
            categroy_q = Q(category__parent_category__parent_category=c1)
            if c2:
                categroy_q = Q(category__parent_category=c2)
                if c3:
                    categroy_q = Q(category=c3)
        com_q = Q()
        if com:
            com_q = Q(company__name__icontains=com)
        b_q = Q()
        if b:
            b_q = Q(brand__name__icontains=b)
        s_q = Q()
        if s:
            s_q = Q(series__name__icontains=b)
        ct_q = Q()
        if ct1 or ct2:
            ct_q = Q(create_time__gt=df, create_time__lt=dt)
        select_q = Q(type=type, active=1)

        products = Product.objects.select_related('brand', 'series',
                                                  'company',
                                                  'category',
                                                  'category__parent_category',
                                                  'category__parent_category__parent_category').filter(
            kw_q, com_q, b_q, pn_q, categroy_q, s_q,
            ct_q, select_q).order_by(
            '-id')
        if order == 'n':
            products = products.extra(select={
                'gbk_title': 'convert(`products_product`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (desc == 0 and '-' or ''))
        elif order == 'pn':
            products = products.extra(select={
                'gbk_title': 'convert(`products_product`.`product_no` using gbk)'}).order_by(
                '%sgbk_title' % (desc == 0 and '-' or ''))
        elif order == 'c1':
            products = products.order_by(
                '%scategory__parent_category__parent_category__name' % (
                    desc == 0 and '-' or ''))
        elif order == 'c2':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productcategory`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (desc == 0 and '-' or ''))
        elif order == 'c3':
            products = products.order_by(
                '%scategory__parent_category__name' % (
                    desc == 0 and '-' or ''))
        elif order == 'c':
            products = products.extra(select={
                'gbk_title': 'convert(`customers_company`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (desc == 0 and '-' or ''))
        elif order == 'b':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productbrand`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (desc == 0 and '-' or ''))
        elif order == 's':
            products = products.extra(select={
                'gbk_title': 'convert(`products_productbrandseries`.`name` using gbk)'}).order_by(
                '%sgbk_title' % (desc == 0 and '-' or ''))
        elif order == 'd':
            products = products.order_by(
                '%screate_time' % (desc == 0 and '-' or ''))
        # print order_key

        result = []

        per_page = 15

        try:
            p = Paginator(products, per_page)
            page = p.page(page_id)
            pages = p.num_pages
            try:
                next_page = Paginator(products, per_page).page(
                    page_id + 1).has_next()
            except:
                next_page = False
            for product in page.object_list:
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
                result.append({
                    "id": product.id if not kw else change_style(
                        str(product.id), kw.strip()),
                    "name": product.name if not kw else change_style(
                        product.name, kw.strip()),
                    "product_no": product.product_no if not kw else change_style(
                        product.product_no,
                        kw.strip()),
                    "brand": brand_name if not kw else change_style(
                        brand_name, kw.strip()),
                    "series": series_name if not kw else change_style(
                        series_name, kw.strip()),
                    "c1": c1 if not kw else change_style(c1,
                                                              kw.strip()),
                    "c2": c2 if not kw else change_style(c2,
                                                              kw.strip()),
                    "c3": c3 if not kw else change_style(c3,
                                                              kw.strip()),
                    "company": company_name if not kw else change_style(
                        company_name, kw.strip()),
                    "style": style if not kw else change_style(style,
                                                                    kw.strip()),
                    "create_time": ctime if not kw else change_style(ctime,
                                                                          kw.strip()),
                    "update_time": utime if not kw else change_style(utime,
                                                                          kw.strip()),
                    "charlet": charlet,
                    "status": product.status,
                    "status_string": product.status and '启用' or '禁用',
                })
            return Response(result,status=status.HTTP_200_OK)
                # products.reverse()
        except Exception as e:
            print e.message
            page = 0
            pages = 0
            next_page = False
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        p = Product.objects.get(id=pk)
        product = {
            "id": p.id,
            "product_no": p.product_no,
            "product_name": p.name or 'N/A',
            "company_name": p.company and p.company.name or 'N/A',
            "category_name": get_category(p.category_id) or 'N/A',
            "brand": p.brand and p.brand.name or 'N/A',
            "series": p.series and p.series.name or 'N/A',
            "args": {},
            "remarks": p.remark or 'N/A',
            "norm_no": p.norms_no or 'N/A',
            "version": p.version_no or 'N/A',
            # "model_name": model.name,
            "length": str(p.length),
            "width": str(p.width),
            "height": str(p.height),
            "material": p.material or 'N/A',
            "color": p.color or 'N/A',
            'chartlet': p.chartlet_path,
            'files': [],
            'previews': []
        }
        for file in p.files.all().order_by('-id'):
            product['files'].append({
                'id': file.id,
                'name': file.name,
                'url': file.file.url,
                'preview': file.preview.url
            })
        for preview in p.previews.all().order_by('-id'):
            product['previews'].append({
                'id': preview.id,
                'name': preview.name,
                'url': preview.file.url
            })
        product['args'] = json.loads(p.args.decode('utf-8'))
        return Response(product,status=status.HTTP_200_OK)

    @detail_route(methods=['post','get'])
    def void(self, request, pk=None):
        Product.objects.filter(pk=pk).update(status=0)
        return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post','get'])
    def active(self, request, pk=None):
        Product.objects.filter(pk=pk).update(status=1)
        return Response(status=status.HTTP_200_OK)
