# -*-coding:utf8-*-

"""
视图文件


"""

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
