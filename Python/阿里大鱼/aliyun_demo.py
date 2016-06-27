# -*- coding: utf-8 -*-
import top.api
import urllib2
import json

req = top.api.AlibabaAliqinFcSmsNumSendRequest("http://gw.api.taobao.com/router/rest")
req.set_app_info(top.appinfo("23383389","b6c0fab4a72c545da04155966faf0221"))

req.extend="123456"
req.sms_type="normal"
req.sms_free_sign_name="测试签名"
req.sms_param="{\"code\":\"1234\",\"product\":\"pride1952\"}"
req.rec_num="18610583280"
req.sms_template_code="SMS_10391034"

temp = req.getResponse()
sock = urllib2.urlopen(url="http://gw.api.taobao.com"+temp["url"], data=temp["body"])
doc = sock.readlines()

jj = json.loads(doc[0])


print doc