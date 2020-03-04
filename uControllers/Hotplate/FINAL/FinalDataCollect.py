# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:00:27 2019

@author: maxhu
"""

import RPi.GPIO as GPIO
import time
import uControllersDataAcquisition as DtA
#====================================================================#
#This segment of code deals with setting up GPIO pins for the MCP
GPIO.setmode(GPIO.BOARD)

CS = [29, 32, 18, 8]
CLK = [31, 36, 22, 10]
DOUT = [33, 38, 24, 12]
DIN = [37, 40, 26, 16]

for i in range(0,4):
    GPIO.setup(CS[i], GPIO.OUT)
    GPIO.setup(CLK[i], GPIO.OUT)
    GPIO.setup(DOUT[i], GPIO.IN)
    GPIO.setup(DIN[i], GPIO.OUT)
#====================================================================#
#This creates two lists of lists that can hold 25 different sets of 
#data
TEMP = [[] for i in range(0,25)]   
TIME = [[] for i in range(0,25)]
#====================================================================#
#Here is where the magic happens... **--*-***---*
try:
    my_test = True
    start_time = time.time()
    while my_test == True:
        #This is in charge of ending the program in case a sensor
        #exceeds 100C and ensures data is making sense for user.
        test = DtA.calc_tempMCPBudgetLM34(DtA.readMCP(0, CS[0], CLK[0],
        DOUT[0], DIN[0]))
        print(test)
        test = float(test)
        if test > 100:
            break
        #These two loops go through each MCP(i) and each MCP channel (n)
        for i in range(0,4):
            for n in range(0,8):
                if i == 3 and n == 1: #last channel of the last MCP that 
                    #needs data
                    break
                #It reads from a function defined in data acquisition file
                d = DtA.readMCP(n, CS[i], CLK[i], DOUT[i], DIN[i])
                TIME[8 * i + n].append(time.time() - start_time)
                t = DtA.calc_tempMCPBudgetLM34(d)
                TEMP[8 * i + n].append(t)
#====================================================================#
#This writes data to a file
        file = open('./Data/HOTPLATETESTING.txt', 'w')
        for i in range(0,25):
            for n in range(0,len(TIME[i])):
                file.write(str(TIME[i][n]) + ',' + TEMP[i][n] + '\n')
        file.close()
        
except KeyboardInterrupt:
    print("It's fried, dude.")
    
finally:
    GPIO.cleanup()
    print('Isaac cleaned the oven')