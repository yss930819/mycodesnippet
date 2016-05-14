import urllib2
import urllib
import time
url='http://course.buaa.edu.cn/'
import os

def cut():
    os.popen('taskkill /f /im SangforCSClient.exe')
    os.popen('taskkill /f /im SangforPromoteService.exe')
    os.popen('taskkill /f /im SangforUD.exe')
    os.popen('taskkill /f /im SangforServiceClient.exe')
#print 'connecting....'
#status = os.popen('taskkill /f /im SangforCSClient.exe')
#time.sleep(10)
#status = os.popen('"C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe"')
#time.sleep(20)
while 1:
    for i in range(0,7200):
        try:
            os.popen('del/f/s/q C:\Program Files (x86)\Sangfor\SSL\SangforUpdate\SangforUD.exe')
            urllib2.urlopen(url).read()
            print 'connected'
            time.sleep(200)
        except Exception as e:
            cut()
            print e
            print 'connecting....'
            time.sleep(20)
            status = os.popen('"C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe"')
            time.sleep(20)
    
    print 'connecting....'
    cut()
    time.sleep(10)
    status = os.popen('"C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe"')
    time.sleep(20) 
