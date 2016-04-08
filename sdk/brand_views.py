from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from products.models import ProductCategory
from products.product_utils import *
from rest_framework import status
from rest_framework.response import Response
from customers.models import Company
from products.models import ProductBrand, ProductBrandSeries


class BrandViewSet(viewsets.ViewSet):
    def list(self, request):
        cid = request.GET.get('cid', 0)
        if not cid:
            return Response(status=status.HTTP_404_NOT_FOUND)
        result = []
        comps = Company.objects.prefetch_related('brands','brands__series').all()
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
        return Response(get_brand_series(pk),status=status.HTTP_200_OK)