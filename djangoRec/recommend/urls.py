# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/27 9:55
@File ：urls.py
@IDE ：PyCharm
@Author ： KirkQI

"""
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index_view),
    path('main/',views.mian_view),
    path('count101/',views.count101_view),
    path('count107/',views.count107_view),
    path('pagetitlecategoryname/',views.pagetitlecategoryname_view),
    path('pagetitlekw/',views.pagetitlekw_view),
    path('realip/',views.realip_view),
    path('source/',views.source_view),
    path('timestamp/',views.timestamp_view),
    path('useragent/',views.useragent_view),
    path('useros/',views.useros_view),
    path('webinfocount/',views.webinfocount_view),
    path('ymd/',views.ymd_view),
]