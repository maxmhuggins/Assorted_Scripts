# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:33:32 2019

@author: maxhu
"""

#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        MCP4911_sinewave.py
# Purpose:     Generate a sinewave
#
# Author:      paulv
#
# Created:     18-09-2015
# Copyright:   (c) paulv 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import spidev
from time import sleep
import numpy as np

N = 12

DEBUG = False
spi_max_speed = 4 * 1000000 # 4 MHz
V_Ref = 3300 # 3V3 in mV
Resolution = 2**N # 12 bits for the MCP 4921
CE = 0 # CE0 or CE1, select SPI device on bus

# setup and open an SPI channel
spi = spidev.SpiDev()
spi.open(0,CE)
spi.max_speed_hz = spi_max_speed


def setOutput(val):
    # lowbyte has 8 data bits
    # B7, B6, B5, B4, B3, B2, B1, B0
    # D7, D6, D5, D4, D3, D2, D1, D0
    lowByte = val & 0b11111111
    # highbyte has control and 4 data bits
    # control bits are:
    # B7, B6,   B5, B4,     B3,  B2,  B1,  B0
    # W  ,BUF, !GA, !SHDN,  D11, D10, D9,  D8
    # B7=0:write to DAC, B6=0:unbuffered, B5=1:Gain=1X, B4=1:Output is active
    highByte = ((val >> 6) & 0xff) | 0b0 << 7 | 0b0 << 6 | 0b1 << 5 | 0b1 << 4
    #
    # by using spi.xfer2(), the CS is released after each block, transferring the
    # value to the output pin.
    if DEBUG :
        print("Highbyte = {0:12b}".format(highByte))
        print("Lowbyte =  {0:12b}".format(lowByte))
    spi.xfer2([highByte, lowByte])

try:
    while(True):
        for angle in range(1, 360):
            # generate a sine wave
            val = np.sin(angle * ((2 * np.pi) / 360))
            # results in values between -1 and +1
            # add 1 to make all values positive (so between 0 and 2)
            # scale it to get only positive numbers between 0 and 256
            # Use only integer numbers
            val = int((val + 1 ) * 2**N / 8)

            if DEBUG : 
                print("Output value is {0:12b}".format(val))

       	    setOutput(val)

            if DEBUG :
                sleep(0.2)
            else :
                # if you use a DMM to track the output, leave the sleep in.
                # if you use a scope, set the sleep to 0.0
                sleep(0.0)
            print(val)

except KeyboardInterrupt:
    print("Closing SPI channel")
    spi.close()

def main():
    pass

if __name__ == '__main__':
    main()