# -*- coding:utf-8  -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Page(models.Model):
    """
    页面表单

    表单页
    pagename 页面名
    """
    page_name = models.CharField(max_length=10)

    def __unicode__(self):
        return u"%s" % self.pagename


class PageInfo(models.Model):
    """
    每个车票要保存的信息


    """
    page = models.ForeignKey(Page)
    taxi_num = models.CharField(max_length=10, unique=True)
    fee = models.FloatField()
    change_time = models.DateTimeField(auto_now=True)
