#!/usr/bin/env python3
# coding = 'utf-8'
import os
import time

time.sleep(3)
#system('python3 /home/pi/pistreaming/server.py')
a = os.popen('cd /home/pi/pistreaming;python3 server.py').read()
print(a)