# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from products.models import ProductBrand, ProductBrandSeries, CategoryManufactor, ManufactorBrand, Manufactor


class ManufactorViewSet(viewsets.ViewSet):
    def list(self, request):
        comps = Manufactor.objects.filter(active=True)
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
        return Response(get_manufactor_brands(category_id, pk),status=status.HTTP_200_OK)

    def create(self, request):
        name = request.POST.get('name').strip()
        category_id = request.POST.get('category_id', 0)
        if name == '':
            return Response(
                {'success': 0, 'message': '厂家名不能为空'},status=status.HTTP_200_OK)
        category = ProductCategory.objects.get(pk=category_id)
        max_no = 1
        if Manufactor.objects.exists():
            max_no = Manufactor.objects.all().order_by('-no')[0].no + 1
        manufactor_dict = {'id': 0, 'name': name}
        manufactor, flag = Manufactor.objects.get_or_create(name=name)
        if manufactor.no == 0:
            manufactor.no = max_no
            manufactor.save()
        CategoryManufactor.objects.get_or_create(category=category,
                                              manufactor=manufactor)
        manufactor_dict['id'] = manufactor.id
        return Response({'success': 1, 'manufactor': manufactor_dict},status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        category_id = request.POST.get('category_id',0)
        category = ProductCategory.objects.get(pk=category_id)
        manufactor = Manufactor.objects.get(pk=pk)
        CategoryManufactor.objects.filter(manufactor=manufactor,
                                       category=category).delete()
        return Response({'success': 1},status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def batch_delete(self, request):
        category_id = request.POST.get('category_id', 0)
        category = ProductCategory.objects.get(pk=category_id)
        manufactors = Manufactor.objects.filter(
            pk__in=request.POST.get('ids').split(','))
        for manufactor in manufactors:
            CategoryManufactor.objects.filter(manufactor=manufactor,
                                           category=category).delete()
        return Response({'success': 1},status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        name = request.POST.get('name').strip()
        if name == '':
            return Response(
                {'success': 0, 'message': '厂家名不能为空'},status=status.HTTP_200_OK)
        exists_manufactor = Manufactor.objects.filter(name=name).exclude(
            pk=pk)
        manufactor = Manufactor.objects.get(pk=pk)
        if exists_manufactor.exists():
            exists_manufactor = exists_manufactor[0]
            manufactor_categories = manufactor.categories.all()
            manufactor_brands = manufactor.brands.all()
            for category in manufactor_categories:
                CategoryManufactor.objects.get_or_create(manufactor=exists_manufactor,
                                                      category=category)
            for brand in manufactor_brands:
                ManufactorBrand.objects.get_or_create(manufactor=exists_manufactor,
                                                   brand=brand)
            manufactor.categorymanufactor_set.all().delete()
            manufactor.manufactorbrand_set.all().delete()
            manufactor.delete()
            return Response(
                {'success': 2, 'manufactor_id': exists_manufactor.id},status=status.HTTP_200_OK)
        else:
            manufactor.name = name
            manufactor.save()
            return Response({'success': 1},status=status.HTTP_200_OK)