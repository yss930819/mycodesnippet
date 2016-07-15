#-*- encoding:UTF-8 -*
import os
import sys
import string
import psutil
import re
from subprocess import PIPE

p1 = psutil.Popen("", stdout=PIPE)
print p1.poll()

print p1.pid
