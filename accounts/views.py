# -*- encoding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
try:
    import simplejson as json
except:
    import json
import time
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from gezbackend.utils import get_random_code
from django.db.models import Q
from gezbackend.utils import get_password
from .models import Account

class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return super(LoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Account.objects.filter(Q(username=username)|Q(
                email=username))
            if not user.exists():
                return HttpResponse(json.dumps({
                        'result': 1,
                        'message': '',
                        'data': ''
                    }))
            user = user[0]
            user = authenticate(username=user.username, password=password)
            if not user:
                # 登录密码错误
                return HttpResponse(json.dumps({
                    'result': 1,
                    'message': '',
                    'data': ''
                }))
            login(request, user)
            if hasattr(user, 'admin'):
                admin = user.admin
                request.session['token'] = get_random_code(64)
                request.session['uid'] = user.id
                request.session['awid'] = admin.work_id

                # 登录成功
                return HttpResponse(json.dumps({
                    'result': 0,
                    'message': '',
                    'data': ''
                }))
            else:
                # 当前帐户不是系统管理员
                return HttpResponse(json.dumps({
                    'result': 1,
                    'message': '',
                    'data': ''
                }))

        except Exception as E:
            print str(E)
            return HttpResponse(json.dumps({
                'result': 1,
                'message': '',
                'data': ''
            }))