# Max Huggins
# 1/30/19
# Intro to data logging via cap discharge with ADC

import RPi.GPIO as GPIO
import time

#set ADC0831 pins
CS = 29
CLK = 31
DO = 33

#Set capacitor pin
cap = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DO, GPIO.IN)
GPIO.setup(cap, GPIO.OUT)

#define a function to handle reading ADC data
def readADC():
    #set initial binary to as empty
    d = ''
    #Begin conversation with ADC
    GPIO.output(CS,False)
    #oneclock pulse
    #set CLK low
    GPIO.output(CLK,False)
    #Set clk high
    GPIO.output(CLK,True)
    GPIO.output(CLK,False)
    #end CLK pulse
    #now to read data synced to more clokc pulses
    for n in range(0,8): #read in 8 bits, 0-7
        #one clock pulse
        #set CLK low then high
        GPIO.output(CLK,False)
        GPIO.output(CLK,True)
        GPIO.output(CLK,False)
        DO_state = GPIO.input(DO)
        if DO_state == True:
            d = d+'1'
        else:
            d = d + '0'
        #Do until all bits are read
    #End convo w/ ADC
    GPIO.output(CS,True)
    #Return binary
    return d
#define a function to return voltage
def calc_volts(d):
    d_int = int(d,2)
    #Pi goes 0-5V and ADC returns values from 0 -> 255 in binary
    volts = 5.0 * d_int / 255
    #Step per binary # is 5V/255lvls
    volts = round(volts,2)
    return volts
try:
    #Create data arrays
    time_data = []
    voltage_data = []
    #run time for experiment
    run_time = .1
    #charging cap
    GPIO.output(cap,True)
    time.sleep(.5)

    my_test = True

    #Discharge cap and record data
    GPIO.output(cap, False)
    start_time = time.time()
    while my_test == True:
        #append time data
        time_data.append(time.time() - start_time)
        #Call function to read a binary data value
        d = readADC() #This returns the binary data
        #append the binary data
        voltage_data.append(d)
        if time.time() - start_time > run_time:
            my_test = False
    #open a data file for writing in the same directory as the working program
    file = open('CapData30k.txt', 'w')
    for n in range(len(time_data)):
        my_volts = calc_volts(voltage_data[n])
        #Write the data as comma delimites
        file.write(str(time_data[n]) + ',' + str(my_volts) + '\n')
    #always close the file you are using

    file.close()

except KeyboardInterrupt:
    print("It's all over...")

finally:
    GPIO.cleanup()
