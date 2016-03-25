# -*- encoding: utf-8 -*-
import hashlib, re
try:
    import simplejson as json
except:
    import json
from os import urandom
from random import choice
from django.http import HttpResponse
import time

def get_random_code(length = 8, symbol=False):
    """generate a security key"""

    char_set = {
        'nums': '0123456789',
        'small': 'abcdefghijklmnopqrstuvwxyz',
        'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    }

    if symbol:
        char_set['other'] = '!@#$%&*()+?<>'

    password = []

    while len(password) < length:
        key = choice(char_set.keys())
        a_char = urandom(1)
        if a_char in char_set[key]:
            if on_check_previous_char(password, char_set[key]):
                continue
            else:
                password.append(a_char)
    return ''.join(password)


def on_check_previous_char(password, current_char_set):
    """检测前一个字符是否跟生成的一样"""

    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False


def get_password(password, security):
    return hashlib.sha1(hashlib.md5(password).hexdigest() + hashlib.sha1(security).hexdigest()).hexdigest()


def on_check_username(username):
    pattern = re.compile(ur'[a-zA-Z0-9\.\-_]{6,32}$', re.I | re.M)

    if pattern.match(username) == None:
        return False
    return True

def on_check_password(password):
    pass


def on_check_email(email):
    pattern = re.compile(ur'^([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{1,50}){0,5})+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{1,4}){1,3})$$', re.I | re.M)

    if pattern.match(email) == None:
        return False
    return True


def scape_html(html):
    return str(html).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;').replace('\r\n', '<br/>').replace('\r', '<br/>').replace('\n', '<br/>')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def response(result, msg, data):
    return json.dumps({
        "result": result,
        "message": msg,
        "data": data
    })


def resp(result, msg, data, code=200):
    return HttpResponse(response(result, msg, data), content_type="application/json", status=code)


if __name__ == '__main__':
    # print hashlib.sha1('3182318').hexdigest()
    print get_random_code(32)
    # print getPassword('b73ef3b4366a01c916c4695d41f9c19b', 'H2eZlNx8Wn')