#Exam 1
#Feb 11, 2019
#Max Huggins

import RPi.GPIO as GPIO
import time
import uControllersDataAcquisition as DtA

GPIO.setmode(GPIO.BOARD)
CS = 29
CLK = 31
DO = 33

#define a function to handle reading ADC data
d = DtA.readADC()

#define a function to return voltage
DtA.calc_voltsADC(d)

try:
    #Create data arrays
    time_data = []
    voltage_data = []
    #Begin test
    my_test = True
    ready = 'N'
    while ready == 'N':
        print("Are you ready to begin recording? (Y/N)")
        ready = input()
        if ready == 'Y':
            print("Make sure your battery is plugged in. Let's begin our journey!")
    start_time = time.time()
    time.sleep(1)
    while my_test == True:
        #append time data
        time_data.append(time.time() - start_time)
        #Call function to read a binary data value
        d = DtA.readADC() #This returns the binary data
        #append the binary data
        voltage_data.append(d)
        voltage = DtA.calc_volts(d)
        print(voltage)
        if voltage <= 2.4: #stop if under 2.4V (means 9V batt is at 4.8V)
            my_test = False
        else:
            time.sleep(30)
            print(voltage)
    #open a data file for writing in the same directory as the working program
    file = open('Test1NEWCode.txt', 'w')
    for n in range(len(time_data)):
        my_volts = DtA.calc_volts(voltage_data[n])
        #Write the data as comma delimites
        file.write(str(time_data[n]) + ',' + str(my_volts) + '\n')
    #always close the file you are using

    file.close()

except KeyboardInterrupt:
    print("it's fried, dude")

finally:
    GPIO.cleanup()
    print("Isaac cleaned the oven...")
