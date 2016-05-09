# -*- coding:utf-8  -*-

from django.contrib import admin
from .models import PageInfo
from .models import Page

# Register your models here.


# class PageInfoInline(admin.TabularInline):
#     model = PageInfo
#     extra = 3


class PageAdmin(admin.ModelAdmin):
    """
    自定义Page管理页面
    """
    list_display = ['page_name']


class PageInfoAdmin(admin.ModelAdmin):
    """
    自定义对PageInfo的管理页面
    """
    list_display = ['page', 'taxi_num', 'fee', 'change_time']
    search_fields = ['taxi_num', 'page']

    # inlines = [PageInfoInline]


admin.site.register(PageInfo, PageInfoAdmin)
admin.site.register(Page, PageAdmin)