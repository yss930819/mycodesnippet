# -*- coding:utf-8  -*-

# 为了外部调用数据库api
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiechepiao.settings')
import django
django.setup()


from core.models import Page
from core.models import PageInfo


