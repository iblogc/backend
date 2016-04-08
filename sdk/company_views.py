from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from customers.models import Company
from products.models import ProductBrand, ProductBrandSeries


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