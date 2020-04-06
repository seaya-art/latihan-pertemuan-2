#!/usr/bin/env python
# encoding: utf-8

import time

try:
    import importlib.util
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
print("Led pertama menyala")

GPIO.output(24, GPIO.HIGH)
print("Led kedua menyala")

GPIO.output(25, GPIO.HIGH)
print("Led ketiga menyala")

time.sleep(1)

print("Led pertama mati")
GPIO.output(23, GPIO.LOW)

print("Led kedua mati")
GPIO.output(24, GPIO.LOW)

print("Led ketiga mati")
GPIO.output(25, GPIO.LOW)
GPIO.cleanup() 
