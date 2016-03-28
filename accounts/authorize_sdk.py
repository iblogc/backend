#coding:utf-8
from django.http import HttpResponse
from sdk.models import SdkKey as sdk
from Lejuadmin.utils import *
import time
import uuid
import hashlib
import urllib2
import re
import json
import hmac
import base64
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from collections import OrderedDict
REF_PATTERN = re.compile(r"(?<=//)[^/]*")


class SdkLogin(object):

    def whoisclient(self, token):
        self.router = "/public/welcome/sdk?"
        timestamp = str(int(time.time()))
        nonce = str(uuid.uuid4())
        self.echostr = str(uuid.uuid4())
        signature = [token, timestamp, nonce]
        signature.sort()
        signature = "".join(signature)
        signature = hashlib.sha1(signature).hexdigest()

        # url = self.host+self.router+'signature='+signature+'&'+'timestamp='+timestamp+'&'+\
        #       'nonce='+nonce+'&'+'echostr='+self.echostr

        url = 'http://'+self.ip+':8085'+self.router+'signature='+signature+'&'+'timestamp='+timestamp+'&'+\
              'nonce='+nonce+'&'+'echostr='+self.echostr
        print url
        req = urllib2.Request(url)
        try:
            content = urllib2.urlopen(req, timeout=5).read()
        except Exception, e:
            print str(e)
            return HttpResponse(response(2, 'confirm url wrong', ''))

        print "content", content
        # if content.get('echostr', '') != self.echostr:
        if content != self.echostr:
            return False
        return True

    def get_ip(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        return ip

    def decodeurlb64(self, value):
        value = value.replace('-', '+')
        value = value.replace('_', '/')
        return base64.b64decode(value)

    def encodeurlb64(self, value):
        value = base64.b64encode(value)
        value = value.replace('+', '-')
        value = value.replace('/', '_')
        return value

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() != 'post':
            return resp(4003, "method is not post", '', 401)
        # host = request.get_host()
        # referrer = request.META['HTTP_REFERER']
        # print "referrer url is ", referrer
        # referrer = re.compile(REF_PATTERN, referrer)
        # print "referrer is ", referrer
        # check host
        # if referrer != host:
        #     return HttpResponse(response(1, "referrer != host", ""))

        # test ip
        ip = self.get_ip(request)
        # host = sdk.objects.filter(domain=self.host).all()
        host = sdk.objects.filter(domain=ip).all()
        if len(host) == 0:
            return HttpResponse(response(4004, "host wrong", ""), status=401, content_type="application/json")

        # get host second connection
        # if not self.whoisclient(host[0].token):
        #     return HttpResponse(response(1, "host wrong", ""))

        # access_key and secret_key handle
        post = request.POST
        postdata = post.get('postData')
        if not postdata or ':' not in postdata:
            return resp(4001, "postData wrong", "", 401)
        value_list = postdata.split(":")
        client_id = value_list[0]
        app_license = value_list[1]
        access_key = value_list[2]
        token = value_list[3]
        b64value = dict(json.loads(self.decodeurlb64(value_list[4]), object_pairs_hook=OrderedDict))
        print b64value, type(b64value)
        data = ""
        try:
            data = self.encodeurlb64(json.dumps(b64value['data']).replace(" ", ""))
        except Exception, e:
            print str(e)
        try:
            secret_key = sdk.objects.filter(access_key=access_key).all()[0].secret_key
        except IndexError:
            return HttpResponse(response(4000, "no such a access_key", ""), status=401, content_type="application/json")

        sha1_value = self.encodeurlb64(hmac.new(secret_key.encode('utf-8'), data, digestmod=hashlib.sha1).hexdigest())

        if token != sha1_value:
            msg = "access_key or secret_key is wrong"
            data = "server_token is %s token is %s" % (sha1_value, token)
            return HttpResponse(response(4000, msg, data), status=401, content_type="application/json")

        return super(SdkLogin, self).dispatch(request, *args, **kwargs)
