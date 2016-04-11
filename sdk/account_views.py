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
from accounts.serializers import AccountSerializer
from accounts.models import Account
from django.contrib.auth import authenticate, login
from gezbackend.utils import get_random_code
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

@csrf_exempt
@api_view(http_method_names=['post'])
def login(self, request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = Account.objects.filter(Q(username=username) | Q(
            email=username))
        if not user.exists():
            return Response({
                'result': 1,
                'message': '',
                'data': ''
            },status=status.HTTP_200_OK)
        user = user[0]
        user = authenticate(username=user.username, password=password)
        if not user:
            # 登录密码错误
            return Response({
                'result': 1,
                'message': '',
                'data': ''
            }, status=status.HTTP_200_OK)
        login(request, user)
        if hasattr(user, 'admin'):
            admin = user.admin
            request.session['token'] = get_random_code(64)
            request.session['uid'] = user.id
            request.session['awid'] = admin.work_id

            # 登录成功
            return Response({
                'result': 0,
                'message': '',
                'data': ''
            }, status=status.HTTP_200_OK)
        else:
            # 当前帐户不是系统管理员
            return Response({
                'result': 1,
                'message': '',
                'data': ''
            }, status=status.HTTP_200_OK)

    except Exception as E:
        print str(E)
        return Response({
            'result': 1,
            'message': '',
            'data': ''
        }, status=status.HTTP_200_OK)