# -*- coding:utf-8  -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Page(models.Model):
    """
    页面表单

    表单页
    page_name 页面名
    """
    page_name = models.CharField(max_length=10)
    fees = models.FloatField()
    total = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.page_name
        
    def __str__(self):
        return u"%s" % self.page_name


class PageInfo(models.Model):
    """
    每个车票要保存的信息


    """
    
    page = models.ForeignKey(Page)
    taxi_num = models.CharField(max_length=10)
    fee = models.FloatField()
    change_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s,%d" % (self.taxi_num, self.page_id)
    
    
    def __str__(self):
        return u"%s,%d" % (self.taxi_num, self.page_id)
