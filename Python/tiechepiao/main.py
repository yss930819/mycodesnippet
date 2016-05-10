# -*- coding:utf-8 -*-

"""
主要使用文件
调用了django的一些东西
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiechepiao.settings')
import django
django.setup()

from core.models import Page, PageInfo



def GetAllPage():
    """
    获取全部page信息
    """
    ps = Page.objects.all()
    for p in ps:
        print(p.page_name)
    return ps
    
def GetPage(page_name):
    """
    获取page信息
    """
    p = Page.objects.filter(page_name=page_name)
    if len(p):
        print("%s" % p[0].page_name)
    return p


def SavePage(page_name):
    """
    保存页面
    """
    ret = 0
    try:
        page = Page(page_name=page_name, fees=0.0 ,total=0)
        page.save()
        print("Page:%s创建成功" % page.page_name)
        ret = 1
    except Exception as error:
        print(error)
        ret = 0
    return ret

def SavePageInfo(page, taxi_num, fee):
    """
    保存页面
    """
    ret = 0
    if not IsExistTaxiNum(page, taxi_num):
        try:
            page_info = PageInfo(page=page, taxi_num=taxi_num, fee=fee)
            page.fees = page.fees + float(fee)
            page.total = page.total + 1
            page.save()
            page_info.save()
            print("fees:%.2f total:%d  num:%s  fee：%s" % (page.fees,page.total,page_info.taxi_num,page_info.fee))
            ret = 1
        except Exception as error:
            print(error)
            ret = 0
    else:
        print("已存在！")
        ret = -1;
    return ret

def AllFees(page):
    page_infos = PageInfo.objects.filter(page=page)
    sum = 0.0
    for page_info in page_infos:
        print(page_info.fee)
        sum = page_info.fee + sum
    return sum
    
    
def IsExistTaxiNum(page, taxi_num):
    """
    判断是否存在车牌号
    """
    page_infos = PageInfo.objects.filter(page=page, taxi_num=taxi_num)
    return len(page_infos)

def addPageInfos(page):
    """
    循环直到收到e
    """
    while True:
        ss = input("pageinfo输入:")
        args = ss.split(" ")
        if ss == "e":
            break
        elif len(args) == 2:
            SavePageInfo(page,args[0],args[1])
        else:
            print("输入错误！！！")

def DisplayPages():
    ps = GetAllPage()
    for p in ps:
        print(p.page_name, ":", p.fees,":" ,p.total)
    return 1            
            
def menu():
    while True:
        ss = input("menu输入:")
        args = ss.split(" ")
        if args[0] == "e":
            break
        elif args[0] == "list":
            DisplayPages()
        elif args[0] == "page":
            if not len(GetPage(args[1])):
                SavePage(args[1])
            else:
                print("已存在！！")
        elif args[0] == "add":
            addPageInfos(GetPage(args[1])[0])
        else:
            print("错误的参数：%s" % args[0])
            
            

if __name__ == "__main__":
    """
    主函数
    """
    # p = Page(page_name="1")
    # p.save()
    # ps = GetAllPage()
    # # ss = input("输入:")
    # # args = ss.split(" ")
    # # SavePageInfo(ps[0],args[0],args[1])
    # # print(AllFees(ps[0]))    
    # addPageInfos(ps[0])
    menu()