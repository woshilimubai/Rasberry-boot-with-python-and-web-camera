#!/usr/bin/env python3
# coding = 'utf-8'
import RPi.GPIO as GPIO
from os import system
import time

time.sleep(30)
def fun(arg):
    #GPIO.cleanup()
    print(arg)
    system('sudo halt')
    print('success')


GPIO.setmode(GPIO.BOARD)
GPIO_PIN=12 #将有内存卡的一端朝上，右边一排的第六个排针
GPIO.setup(GPIO_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(GPIO_PIN,GPIO.FALLING,bouncetime=2000,callback=fun
                      )
while True:
    pass
