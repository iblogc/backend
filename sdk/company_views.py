# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from customers.models import Company
from products.models import ProductBrand, ProductBrandSeries, CategoryCompany


class CompanyViewSet(viewsets.ViewSet):
    def list(self, request):
        comps = Company.objects.filter(active=True)
        result = []
        for comp in comps:
            result.append({
                'id':comp.id,
                'name':comp.name
            })
        return Response(result,
                        status=status.HTTP_200_OK)

    @detail_route()
    def brands(self, request, pk=None):
        category_id = request.GET.get('category_id', 0)
        return Response(get_company_brands(category_id, pk),status=status.HTTP_200_OK)

    def create(self, request):
        name = request.POST.get('name').strip()
        category_id = request.POST.get('category_id', 0)
        if name == '':
            return Response(
                {'success': 0, 'message': '厂家名不能为空'},status=status.HTTP_200_OK)
        category = ProductCategory.objects.get(pk=category_id)
        max_no = 1
        if Company.objects.exists():
            max_no = Company.objects.all().order_by('-no')[0].no + 1
        company_dict = {'id': 0, 'name': name}
        company, flag = Company.objects.get_or_create(name=name)
        if company.no == 0:
            company.no = max_no
            company.save()
        CategoryCompany.objects.get_or_create(category=category,
                                              company=company)
        company_dict['id'] = company.id
        return Response({'success': 1, 'company': company_dict},status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        category_id = request.POST.get('category_id',0)
        category = ProductCategory.objects.get(pk=category_id)
        company = Company.objects.get(pk=pk)
        CategoryCompany.objects.filter(company=company,
                                       category=category).delete()
        return Response({'success': 1},status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def batch_delete(self, request):
        category_id = request.POST.get('category_id', 0)
        category = ProductCategory.objects.get(pk=category_id)
        companies = Company.objects.filter(
            pk__in=request.POST.get('ids').split(','))
        for company in companies:
            CategoryCompany.objects.filter(company=company,
                                           category=category).delete()
        return Response({'success': 1},status=status.HTTP_200_OK)