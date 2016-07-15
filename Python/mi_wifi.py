# -*-coding=utf8

"""
作者：yss
创建时间：2016-4-23

短信验证码发送模块
调用短信平台  http://www.leilaohu.cn/  的webserver。


包含方法如下：
create_validated_code: 随机生成6位数字验证码。
url_post_webserver： 发送webserver请求函数，post方法
leilaohu_send_validated_code： 雷老虎短信平台发送验证码短信
leilaohu_sendsms1_send: 雷老虎短信平台发短信功能
leilaohu_getbalance: 雷老虎平台余额查询
leilaohu_getmo： 雷老虎平台获取用户回复

"""
# 导入模块
import random
# url 连接模块
import urllib
import urllib2
# xml解析
from xml.dom.minidom import parseString
import xml.dom

# 解决编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# *******************************
# 要使用的常量
# ********************************

# ++++++++++++++++++++++++++++++++
# 使用的URL
# ++++++++++++++++++++++++++++++++
url_001 = "http://miwifi.com/cgi-bin/luci/;stok=50a5e869dbc0c33b2442e06c35205c79/api/xqsystem/set_name_password"
url_002 = "http://miwifi.com/cgi-bin/luci/;stok=ea73835ba5723ba6e03a818bdc476ce3/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3B%2Fusr%2Fsbin%2Ftelnetd"
# *******************************
# 常量结束了！ (～￣▽￣)～
# ********************************


def url_post_webserver(url, post_data, code='utf-8'):
    """
    进行post请求，相对于webserver
    对返回情况也有处理
    :param url: 请求的url
    :param post_data: 发给请求的post
    :return:返回xml,可以使用xml进行解析
    """
    page = urllib2.urlopen(url, post_data)
    lines = page.readlines()
    page.close()
    document = ""
    for line in lines :
        document = document + line.decode(code)
    return document

def mi_wifi():
    """
    获取用户的回复消息

    乱码问题解决
    :return:  暂时错误信息，和一串字符（保存了用户回复的消息）
                字符结构如下
               【nnn,xxx；nnn,xxx】 nnn表示手机号，xxx表示信息 两条信息中间使用分号分割
               “18810680819,%c4%e3%ba%c3;18810680819,%d4%da%c2%f0%a3%bf”
               “”
    """

    data = {}
    data["oldPwd"] = "tdcqadmin@1"
    data["oldPwd"] = "admin"

    post_data = urllib.urlencode(data,)
    doc = url_post_webserver(url_001, post_data)

    dom = parseString(doc)
    
    ret = doc
    
    return dom

# 模块测试

if __name__ == "__main__":
    # Phone = "18810680819"
    # code = create_validated_code()
    # ll = leilaohu_send_validated_code(code, Phone)
    # print ll[0]
    # print ll[1]
    ll = mi_wifi()
    print ll

    # str_dd = "18810680819,%c4%e3%ba%c3+;18810680819,%b1%b1%ba%bd%d0%c2%cf%ca%ca%c2"
    # print urllib.unquote(str_dd).decode("gbk")
