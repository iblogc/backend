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
from braces.views import LoginRequiredMixin
from customers.serializers import CustomerAccountSerializer
from customers.models import CustomerAccount

class CustomerAccountViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerAccountSerializer
    queryset = CustomerAccount.objects.all()