# Create your views here.
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *


def index_view(request):
    return render(request, 'index.html')


def mian_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    if u and p:
        c = RecommendStudentinfo.objects.filter(stu_name=u, stu_pwd=p).count()
        if c >= 1:
            return HttpResponse("登陆成功!")
        else:
            return HttpResponse("账号密码错误!")
    else:
        return HttpResponse("请输入账号密码!")


def count101_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    count101web = Count101Web.objects.all()
    print(count101web.query)  # 打印查询时使用的语句
    print(type(count101web))  # 打印查询结果的数据类型
    for user in count101web:
        print("%s-->%s" % (user.type, user.num))
    result["data"] = serializers.serialize('python', count101web)
    return JsonResponse(json.dumps(result), safe=False)


def count107_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    count107web = Count107Web.objects.all()
    print(count107web.query)  # 打印查询时使用的语句
    print(type(count107web))  # 打印查询结果的数据类型
    for user in count107web:
        print("%s-->%s" % (user.type, user.num))
    result["data"] = serializers.serialize('python', count107web)
    return JsonResponse(json.dumps(result), safe=False)


def fullurl_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    fullurl = Fullurl.objects.all()
    print(fullurl.query)  # 打印查询时使用的语句
    print(type(fullurl))  # 打印查询结果的数据类型
    for user in fullurl:
        print("%s-->%s" % (user.fullurl, user.num))
    result["data"] = serializers.serialize('python', fullurl)
    return JsonResponse(json.dumps(result), safe=False)


def onesweb_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    onesweb = OnesWeb.objects.all()
    result["data"] = serializers.serialize('python', onesweb)
    return JsonResponse(json.dumps(result), safe=False)


def pagetitlecategoryname_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    pagetitlecategoryname = Pagetitlecategoryname.objects.all()
    result["data"] = serializers.serialize('python', pagetitlecategoryname)
    return JsonResponse(json.dumps(result), safe=False)


def pagetitlekw_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    pagetitlekw = Pagetitlekw.objects.all()
    result["data"] = serializers.serialize('python', pagetitlekw)
    return JsonResponse(json.dumps(result), safe=False)


def realip_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    realip = Realip.objects.all()
    result["data"] = serializers.serialize('python', realip)
    return JsonResponse(json.dumps(result), safe=False)


def source_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    source = Source.objects.all()
    result["data"] = serializers.serialize('python', source)
    return JsonResponse(json.dumps(result), safe=False)


def timestamp_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    timestamp = Timestamp.objects.all()
    result["data"] = serializers.serialize('python', timestamp)
    return JsonResponse(json.dumps(result), safe=False)


def useragent_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    useragent = Useragent.objects.all()
    result["data"] = serializers.serialize('python', useragent)
    return JsonResponse(json.dumps(result), safe=False)

def useros_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    useros = Useros.objects.all()
    result["data"] = serializers.serialize('python', useros)
    return JsonResponse(json.dumps(result), safe=False)

def webinfocount_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    webinfocount = WebInfoCount.objects.all()
    result["data"] = serializers.serialize('python', webinfocount)
    return JsonResponse(json.dumps(result), safe=False)

def ymd_view(request):
    result = {"message": 'success', "code": '0', "data": []}
    ymd = Ymd.objects.all()
    result["data"] = serializers.serialize('python', ymd)
    return JsonResponse(json.dumps(result), safe=False)
