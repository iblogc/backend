# -*- encoding:utf-8 -*-
try:
    import simplejson as json
except:
    import json
import time
from gezbackend import utils
from accounts.models import Account, AccountLog
from django.http import HttpResponseRedirect, HttpResponse
from system.models import Menu


class AccountLoginMixin(object):

    def dispatch(self, request, *args, **kwargs):
        self.inAjax = request.GET.get('inAjax') if request.GET.get('inAjax') else request.POST.get('inAjax')
        self.isLogin = request.session.get('uid')
        self.path = request.path

        self.openMenu = True if '_LeftMenuOpen_' in request.COOKIES else False

        if self.isLogin == None:
            if self.inAjax == None:
                return HttpResponseRedirect('/accounts/login/')
            else:
                return HttpResponse(json.dumps({
                    'result': 1,
                    'message': 'login out',
                    'data': ''
                }))
        else:
            self.account_id = Account.objects.get(pk=self.isLogin)
            if not self.account_id:
                del request.session['uid']
                del request.session['token']

                if self.inAjax == None:
                    return HttpResponseRedirect('/accounts/login/')
                else:
                    return HttpResponse(json.dumps({
                        'result': 1,
                        'message': 'login out',
                        'data': ''
                    }))

        self.uid = self.account_id.id
        self.username = self.account_id.username
        self.email = self.account_id.email
        self._aciton = request.path_info
        self._url = request.get_full_path()
        self._request = json.dumps({'GET': request.GET, 'POST':request.POST})
        self._response = json.dumps({})
        self._status = 1
        self._ip_address = utils.get_client_ip(request)

        # account Log
        # develop close this function
        # self.accountLog()


        # check user status
        # disabled for develop
        '''
        if self._aciton <> '/':
            if self.account_id.status == 0:
                if self.inAjax is not None:
                    return HttpResponse(json.dumps({
                        'result': 1,
                        'message': '0',
                        'data': ''
                    }))
                else:
                    return HttpResponseRedirect('/')
            elif self.account_id.status == 4:
                if self.inAjax is not None:
                    return HttpResponse(json.dumps({
                        'result': 1,
                        'message': '4',
                        'data': ''
                    }))
                else:
                    return HttpResponseRedirect('/users/appeal/?uid='+self.account_id.id+'&token='+utils.getRandomCode(64))
            '''


        return super(AccountLoginMixin, self).dispatch(request, *args, **kwargs)

    def accountLog(self):
        AccountLog.objects.create(
            actions = self._aciton,
            request = self._request,
            response = self._response,
            url = self._url,
            status = self._status,
            account_id = self.account_id,
            ip_address = self._ip_address,
            create_time = time.time()
        )

    def get_context_data(self, **kwargs):
        context = super(AccountLoginMixin, self).get_context_data(**kwargs)
        context['uid'] = self.uid
        context['email'] = self.email
        context['username'] = self.username
        context['menu'] = self.get_menu()
        context['menuActive'] = self.get_menu_active()
        context['openMenu'] = self.openMenu
        # print self.openMenu
        # print context['menu']

        return context

    def get_menu(self):
        menu = Menu.objects.prefetch_related('sub_menus').filter(parent_menu__isnull=True,
                                    status=1).order_by(
            'sort_id', 'id')
        menuTree = []
        menuTopId = []

        for m in menu:
            menu_dict = {
                'id': m.id,
                'parent_id': m.parent_menu_id,
                'name': m.name,
                'keycode': m.keycode,
                'url': m.url,
                'is_menu': m.is_menu,
                'sort_id': m.sort_id,
                'icon_class': m.icon_class,
                'style_css': m.style_css,
                'childs': []
            }

            for m2 in m.sub_menus.all():
                menu_dict['childs'].append({
                            'id': m2.id,
                            'parent_id': m2.parent_menu_id,
                            'name': m2.name,
                            'keycode': m2.keycode,
                            'url': m2.url,
                            'is_menu': m2.is_menu,
                            'sort_id': m2.sort_id,
                            'icon_class': m2.icon_class,
                            'style_css': m2.style_css
                        })
            menuTree.append(menu_dict)

        # print menuTree
        return menuTree

    def get_menu_active(self):
        self.path = self.path.rstrip('\/')

        try:
            menu = Menu.objects.filter(url=self.path).all()[0]
            parent = Menu.objects.filter(id=menu.parent_id).all()
            activeMenu = {
                'parentId': menu.parent_id,
                'keyCode': menu.keycode,
                'parentKeyCode': parent[0].keycode if parent else menu.keycode
            }

        except Exception as E:
            # print str(E)
            activeMenu = {
                'parentId': 0,
                'keyCode': '',
                'parentKeyCode': ''
            }

        # print activeMenu
        # print self.path.rstrip('\/')
        return activeMenu
