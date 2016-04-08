# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from customers.models import Company
from products.models import ProductBrand, CategoryBrand, CompanyBrand


class SeriesViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def create(self, request):
        name = request.POST.get('name').strip()
        brand_id = request.POST.get('brand_id', 0)
        if name == '':
            return Response(
                {'success': 0, 'message': '系列名不能为空'},status=status.HTTP_200_OK)
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
        return Response({'success': 1, 'series': series_dict},
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        ProductBrandSeries.objects.filter(pk=pk).update(active=False)
        return Response({'success': 1},status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        name = request.POST.get('name').strip()
        if name == '':
            return Response({'success': 0, 'message': '系列名不能为空'},status=status.HTTP_200_OK)
        ProductBrandSeries.objects.filter(pk=pk).update(name=name)
        return Response({'success': 1},status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def batch_delete(self, request):
        ids = request.POST.get('ids').split(',')
        ProductBrandSeries.objects.filter(pk__in=ids).update(active=False)
        return Response({'success': 1}, status=status.HTTP_200_OK)