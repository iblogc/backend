from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(get_categories(),
             status=status.HTTP_200_OK)

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

    