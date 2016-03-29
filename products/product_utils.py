#coding:utf-8
import json
import time
from models import ProductCategory
from django.core.cache import cache

class Node(object):
    def __init__(self, _id, pid, obj):
        self.id = _id
        self.pid = pid
        self.obj = obj
        self.child = []
        self.idorder = ""

    def get_pid(self):
        return self.pid

    def get_id(self):
        return self.id

    def get_obj(self):
        return self.obj

    def add_child(self, node):
        self.child.append(node)

    def get_id_order(self):
        self.idorder += "%s" % self.id

        if len(self.child) == 0:
            return self.idorder

        self.idorder += ','

        for node in self.child:
            if node is self.child[-1]:
                self.idorder += node.get_id_order()
                break
            self.idorder += node.get_id_order()+','
        res = self.idorder
        self.idorder = ""
        return res


class Sortnode(object):

    def __init__(self):
        pass

    def get_sorted_node(self, obj):
        nodelist = {}
        res = []
        for node in obj:
            nodelist[node.id] = Node(node.id, node.parent_id, node)
        root = Node(-1, 0, "")
        for node in nodelist.itervalues():
            if node.get_pid() == 0:
                root.add_child(node)
            else:
                nodelist[node.get_pid()].add_child(node)

        order = root.get_id_order().split(",")[1:]
        for elem in order:
            res.append(nodelist[int(elem)].get_obj())
        return res


class listJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, list):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def get_time(t):
        return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(t))


def get_time_stamp_min(t):
    t = "%s 00:00:00" % t
    t = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(t))


def get_time_stamp_max(t):
    t = "%s 23:59:59" % t
    t = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(t))


def change_style(content, kw):
    return content.replace(kw, '<span style="background:pink">%s</span>' % kw)

TIME_MAX = 2000000000
TIME_MIN = 1000000000


def get_category(c3_id):
    try:
        c3 = ProductCategory.objects.select_related('parent_category', 'parent_category__parent_category').get(id=c3_id, status=1)
        c3_name = c3.name
        c2 = c3.parent_category
        c2_name = c2.name
        c1 = c2.parent_category
        c1_name = c1.name
        return c1_name + '/' + c2_name + '/' + c3_name
    except Exception as e:
        print e.message
        return ''


def get_categories():
    res = []
    if cache.get('category'):
        res = cache.get('category')
    else:
        for c1 in ProductCategory.objects.prefetch_related('sub_categories', 'sub_categories__sub_categories').filter(
                status=1, step=1).all():
            c1_dict = {
                "id": c1.id,
                "name": c1.name,
                "second": []
            }
            res.append(c1_dict)
            for c2 in c1.sub_categories.all():
                c2_dict = {
                    "id": c2.id,
                    "name": c2.name,
                    "third": []
                }
                c1_dict['second'].append(c2_dict)
                for c3 in c2.sub_categories.all():
                    c3_dict = {
                        "id": c3.id,
                        "name": c3.name
                    }
                    c2_dict['third'].append(c3_dict)
        cache.set('category', res)

    return res