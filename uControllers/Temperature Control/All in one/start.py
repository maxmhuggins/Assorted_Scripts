# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:02:49 2019

@author: maxhu
"""

#====================IMPORTS, INITIALIZING, AND HOUSE CLEANING ==============#
import uControllersFunctions as F
import RPi.GPIO as GPIO
import time
import numpy as np

def initial():
    import uControllersFunctions as F
    import RPi.GPIO as GPIO
    import time
    import numpy as np
    
    CONREL = 18
    C = 0
    CS = 32
    CLK = 12
    DOUT = 40
    DIN = 38
    FAN = 22
#============================================================================#
    ref = 3.304
#============================================================================#
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CS, GPIO.OUT)
    GPIO.setup(CLK, GPIO.OUT)
    GPIO.setup(DOUT, GPIO.IN)
    GPIO.setup(DIN, GPIO.OUT)
    GPIO.setup(CONREL,GPIO.OUT)
    GPIO.setup(FAN,GPIO.OUT)
#============================================================================#
    freq = 1
    T_set = 30
    del_t = 0
    
    prop_w_cool = []
    time_w_cool = []
    del_t_w_cool = 0
    
    prop_wo_cool = []
    time_wo_cool = []
    del_t_wo_cool = 0
    
    bang_bang = []
    time_bang = []
    del_t_bang = 0
#============================================================================#
    my_pwm_relay = GPIO.PWM(CONREL, freq)
    my_pwm_fan = GPIO.PWM(FAN, freq)
    duty = 0
    duty_fan = 0
    my_pwm_relay.start(duty)
    my_pwm_fan.start(duty_fan)
#============================================================================#
    def duty_change(error):
        # too cold
        if error > 2:
            duty = 100
            my_pwm_relay.ChangeDutyCycle(duty)
        elif 0 < error < 2:
            duty = 50 * error
            my_pwm_relay.ChangeDutyCycle(duty)
    
        # too hot
        elif error < 0 and error > -2:
            duty_fan = np.abs(50 * error)
            my_pwm_fan.ChangeDutyCycle(duty_fan)
        elif error < -2:
            duty_fan = 100
            my_pwm_fan.ChangeDutyCycle(duty_fan)
#============================================================================#