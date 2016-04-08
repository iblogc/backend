# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(get_categories(),
                        status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def search(self, request):
        kw = request.GET.get('kw').strip()
        per_page = int(request.GET.get('per_page', 50))
        page = int(request.GET.get('page', 1))
        # series = ProductBrandSeries.objects.filter(
        #     Q(name__icontains=kw) | Q(brand__name__icontains=kw) | Q(
        #         brand__companies__name__icontains=kw) | Q(
        #         brand__categories__name__icontains=kw) | Q(
        #         brand__categories__parent_category__name__icontains=kw) | Q(
        #         brand__categories__parent_category__parent_category__name__icontains=kw))
        series = ProductBrandSeries.objects.filter(
            Q(name=kw) | Q(brand__name=kw) | Q(
                brand__companies__name=kw) | Q(
                brand__categories__name=kw) | Q(
                brand__categories__parent_category__name=kw) | Q(
                brand__categories__parent_category__parent_category__name=kw))
        result = []
        for se in series:
            for c3 in se.brand.categories.all():
                for company in se.brand.companies.all():
                    result_dict = {
                        'first_category': c3.parent_category.parent_category.name,
                        'second_category': c3.parent_category.name,
                        'third_category': c3.name,
                        'category_id': c3.id, 'series_id': se.id,
                        'company': company.name, 'brand': se.brand.name,
                        'series': se.name,}
                    if result_dict['first_category'] == kw or result_dict[
                        'second_category'] == kw or result_dict[
                        'third_category'] == kw or result_dict[
                        'company'] == kw or \
                                    result_dict['brand'] == kw or result_dict[
                        'series'] == kw:
                        result.append(result_dict)
        p = Paginator(result, per_page)
        current_page = p.page(page)
        total_pages = p.num_pages
        return Response(
                {'data': current_page.object_list, 'total_pages': total_pages,
                 'current_page': page},status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def sub_categories(self, request, pk):
        return Response(get_sub_categories(pk),
                        status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def companies(self, request, pk):
        return Response(get_category_companies(pk),
                        status=status.HTTP_200_OK)

    @detail_route()
    def brands(self, request, pk=None):
        company_id = request.GET.get('company_id', 0)
        return Response(get_company_brands(pk, company_id),
                        status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def batch_delete(self, request):
        parent_categories = ProductCategory.objects.filter(
            pk__in=request.POST.get('ids').split(','))
        for parent_category in parent_categories:
            if parent_category.sub_categories.exists():
                parent_category.sub_categories.all().update(active=False)
            parent_category.active = False
            parent_category.save()
            parent_category.delete()
        return Response({'success': 1},
                        status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        parent_category = ProductCategory.objects.get(pk=pk)
        if parent_category.sub_categories.exists():
            parent_category.sub_categories.all().update(active=False)
        parent_category.active = False
        parent_category.save()
        return Response({'success': 1},
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        name = request.POST.get('name').strip()
        if name == '':
            return Response(
                {'success': 0, 'message': '分类名不能为空！'},
                status=status.HTTP_200_OK)
        ProductCategory.objects.filter(pk=pk).update(name=name)
        return Response({'success': 1}, status=status.HTTP_200_OK)

    def create(self, request):
        name = request.POST.get('name').strip()
        parent_category_id = request.POST.get('category_id',0)
        if name == '':
            return Response({'success': 0, 'message': '分类名不能为空！'},status=status.HTTP_200_OK)
        step = request.POST.get('step').strip()
        parent_category = ProductCategory.objects.filter(pk=parent_category_id)
        if parent_category.exists():
            parent_category = parent_category[0]
        else:
            parent_category = None
        max_no = 1
        if ProductCategory.objects.filter(step=step).exists():
            max_no = ProductCategory.objects.filter(step=step).order_by('-no')[
                         0].no + 1
        category_dict = {'id': 0, 'name': name}
        category = ProductCategory()
        category.parent_category = parent_category
        category.name = name
        category.step = step
        category.status = 1
        category.no = max_no
        category.save()
        category_dict['id'] = category.id
        return Response({'success': 1, 'category': category_dict},status=status.HTTP_201_CREATED)

    @detail_route()
    def attribute(self, request, pk=None):
        attributes = get_category_attributes(pk)
        return Response(attributes,status=status.HTTP_200_OK)
