import RPi.GPIO as GPIO
import numpy as np

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

###############################################################################################
###############################################################################################

def readADC():
    #set initial binary to as empty
    d = ''
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
        DO_state = GPIO.input(DOUT)
        if DO_state == True:
            d = d+'1'
        else:
            d = d + '0'
        #Do until all bits are read
    #End convo w/ ADC
    GPIO.output(CS,True)
    #Return binary
    return d

###############################################################################################
###############################################################################################

def readMCP(C, CS, CLK, DOUT, DIN):
    d = ''
    #These next few lines start communication with our friends at channel 1
    GPIO.output(CS, False)
    GPIO.output(DIN, True)
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    #######################
    #Input bit selections
    #Sengle ended(not differential)
    #For channel 0 see pg 19 in data sheet
    if C == 0:
        din_control = '1000'
    if C == 1:
        din_control = '1001'
    if C == 2:
        din_control = '1010'
    if C == 3:
        din_control = '1011'
    if C == 4:
        din_control = '1100'
    if C == 5:
        din_control = '1101'
    if C == 6:
        din_control = '1110'
    if C == 7:
        din_control = '1111'
    for n in din_control:
        if n == '1':
            GPIO.output(DIN, True)
        else:
            GPIO.output(DIN, False)
        ###########################
        GPIO.output(CLK, False)
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)
        ###########################
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    ##########################
    #This reads in the data synced to the clock pulses
    for n in range(0,10):
        GPIO.output(CLK, False)
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)
        #Listen to the DOUT pin
        DOUT_state = GPIO.input(DOUT)
        if DOUT_state == True:
            d = d + '1'
        else:
            d = d + '0'
    #Finish talking to MCP
    GPIO.output(CS, True)
    GPIO.output(DIN, False)
    return d

###############################################################################################
###############################################################################################
                 
def calc_voltsMCP(d):
    d_int = int(d,2)
    volts = 5.0*d_int / 1023
    volts = round(volts, 3)
    return volts
                    
###############################################################################################
###############################################################################################

def calc_voltsADC(d):
    d_int = int(d,2)
    volts = 5.0*d_int / 255
    volts = round(volts, 2)
    return volts
                    
###############################################################################################
###############################################################################################

def calc_tempADC_LM34(d):
    d_int = int(d,2)
    #Pi goes 0-5V and ADC returns values from 0 -> 255 in binary
    volts = 5.0 * d_int / 255
    #Step per binary # is 5V/255lvls
    volts = round(volts,2)
    temp = volts / .01
    return temp

###############################################################################################
###############################################################################################

def calc_tempMCP_LM34(d):
    d_int = int(d,2)
    #Pi goes 0-5V and ADC returns values from 0 -> 255 in binary
    volts = 5.0 * d_int / 1023
    #Step per binary # is 5V/255lvls
    volts = round(volts,2)
    temp = volts / .01
    return temp

###############################################################################################
###############################################################################################

V_0 = .5
T_c = .01

def calc_tempMCPBudgetLM34(d):
    d_int = int(d,2)
    volts = 3.307 * d_int / 1023
    T = (np.abs(volts - V_0)) / T_c
    T = round(T, 2)
    T = str(T)
    return T

###############################################################################################
###############################################################################################

R1 = 0
V_input = 0

def calc_tempADC_Thermistor(d):
    d_int = int(d,2)
    #Pi goes 0-5V and ADC returns values from 0 -> 255 in binary
    volts = 5.0 * d_int / 255
    #Step per binary # is 5V/255lvls
    volts = round(volts,2)
    
    #Resistance given by Ohm's law and kirchoff's loop rule
    Resistor_value = (volts * R1)/(V_input - volts)

    #Temperature is a given function with three experimentally determined constants
    temp = (1 / (1.62*10**(-3) + 1.28*10**(-4) * np.log(Resistor_value) + 8.06*10**(-7) * (np.log(Resistor_value))**3)) - 273
    return temp

###############################################################################################
###############################################################################################

def calc_resistADC_Photoresist(d):
    d_int = int(d,2)
    #Pi goes 0-5V and ADC returns values from 0 -> 255 in binary
    volts = 5.0 * d_int / 255
    #Step per binary # is 5V/255lvls
    volts = round(volts,2)
    Resistor_value = (volts * R1)/(V_input - volts)
    if Resistor_value < 15000:
        return Resistor_value
