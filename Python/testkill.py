#-*- encoding:UTF-8 -*
import os
import sys

import psutil
import time
from subprocess import PIPE

p1 = psutil.Popen("python testpid.py",stdin=PIPE,stdout=PIPE)

p1.stdin.write("'yss'\n  '1993'\n")

while p1.is_running():
    pass
print p1.stdout.readlines()

