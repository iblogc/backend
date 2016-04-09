# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from products.models import ProductBrand, CategoryBrand, ManufactorBrand, Manufactor


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

    @detail_route(methods=['get'])
    def attribute_values(self, request, pk=None):
        category_id = request.GET.get('category_id')
        attributes = get_category_attribute_values(category_id, pk)
        return Response(attributes, status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def update_attribute_values(self, request, pk):
        attribute_ids = request.POST.getlist('ids[]')
        attribute_values = request.POST.getlist('values[]')
        attribute_searchable = request.POST.getlist('searchables[]')
        if not len(attribute_ids) == len(attribute_values) == len(
                attribute_searchable):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for index in range(len(attribute_ids)):
            id = attribute_ids[index]
            value = attribute_values[index]
            searchable = int(attribute_searchable[index])
            attribute_value, flag = ProductCategoryAttributeValue.objects.get_or_create(
                attribute_id=id, series_id=pk)
            attribute_value.value = value
            attribute_value.searchable = searchable == 1
            attribute_value.save()
        return Response({'success': 1}, status=status.HTTP_200_OK)