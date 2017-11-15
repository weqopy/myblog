from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json


# Create your views here.
def home(request):
    string_1 = 'Django Learning'
    list_1 = ['HTML', 'Django', 'Python']
    dict_1 = {'first_name': 'Alice', 'last_name': 'Emmy'}
    list_2 = map(str, range(10))
    if_num = 99
    # 字典调用
    # 'string_1': string_1, 后者对应 home 中变量，前者对应 html 文件中变量
    return render(request, 'learn/home.html', {'string_1': string_1, 'list_1': list_1, 'dict_1': dict_1, 'list_2': list_2, 'if_num': if_num})


def temp(request):
    list_3 = ['测试1', '测试2']
    dict_2 = {'a': 3, 4: 'st', 'd_d': '字典测试'}
    return render(request, 'learn/temp.html', {'list_3': list_3})
    # return render(request, 'learn/temp.html', {'list_3': json.dumps(list_3)})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 跳转函数
def old_url_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
        )
