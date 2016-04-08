# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from customers.models import Company
from products.models import ProductBrand, CategoryBrand, CompanyBrand


class BrandViewSet(viewsets.ViewSet):
    def list(self, request):
        cid = request.GET.get('cid', 0)
        if not cid:
            return Response(status=status.HTTP_404_NOT_FOUND)
        result = []
        comps = Company.objects.prefetch_related('brands',
                                                 'brands__series').all()
        for comp_obj in comps:
            res = {}
            res["company_id"] = comp_obj.id
            brand = []

            for elem in comp_obj.brands.all():
                if elem.active == 0:
                    continue
                brand_id = elem.id
                tmp_brand = {}
                tmp_brand['id'] = brand_id
                tmp_brand["name"] = elem.name
                series = []
                for se in elem.series.all():
                    if se.active == 0:
                        continue
                    series.append({
                        "id": se.id,
                        "name": se.name
                    })
                tmp_brand["series"] = series
                brand.append(tmp_brand)
            res["brand"] = brand
            result.append(res)
        return Response(result,
                        status=status.HTTP_200_OK)

    @detail_route()
    def series(self, request, pk=None):
        return Response(get_brand_series(pk), status=status.HTTP_200_OK)

    def create(self, request):
        name = request.POST.get('name').strip()
        category_id = request.POST.get('category_id', 0)
        company_id = request.POST.get('company_id', 0)
        if name == '':
            return Response(
                {'success': 0, 'message': '品牌名不能为空'}, status=status.HTTP_200_OK)
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
        return Response({'success': 1, 'brand': brand_dict},
                        status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        name = request.POST.get('name').strip()
        if name == '':
            return Response(
                {'success': 0, 'message': '品牌名不能为空'}, status=status.HTTP_200_OK)
        ProductBrand.objects.filter(pk=pk).update(name=name)
        return Response({'success': 1},
                        status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        category_id = request.POST.get('category_id', 0)
        company_id = request.POST.get('company_id', 0)
        category = ProductCategory.objects.get(pk=category_id)
        company = Company.objects.get(pk=company_id)
        brand = ProductBrand.objects.get(pk=pk)
        CompanyBrand.objects.filter(company=company, brand=brand).delete()
        CategoryBrand.objects.filter(category=category, brand=brand).delete()
        return Response({'success': 1},
                        status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def batch_delete(self, request):
        category_id = request.POST.get('category_id', 0)
        company_id = request.POST.get('company_id', 0)
        category = ProductCategory.objects.get(pk=category_id)
        company = Company.objects.get(pk=company_id)
        brands = ProductBrand.objects.filter(
            pk__in=request.POST.get('ids').split(','))
        for brand in brands:
            CompanyBrand.objects.filter(company=company, brand=brand).delete()
            CategoryBrand.objects.filter(category=category,
                                         brand=brand).delete()
        return Response({'success': 1},
                        status=status.HTTP_200_OK)