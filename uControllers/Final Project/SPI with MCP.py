#=======================Modules==============================================#
import spidev
import numpy as np
import RPi.GPIO as GPIO
#===========================Constants========================================#
N = 12
C = 0
CS = 32
CLK = 36
DOUT = 40
DIN = 38
#=======================SPI communication protocols=========================#
DEBUG = False
spi_max_speed = 4 * 1000000 # 4 MHz
V_Ref = 3300 # 3V3 in mV
Resolution = 2**N # 12 bits for the MCP 4921
CE_1 = 0 # CE0 or CE1, select SPI device on bus

# setup and open an SPI channel
spi_1 = spidev.SpiDev()
spi_1.open(0,CE_1)
spi_1.max_speed_hz = spi_max_speed

CE_2 = 1 # CE0 or CE1, select SPI device on bus

# setup and open an SPI channel
spi_2 = spidev.SpiDev()
spi_2.open(0,CE_2)
spi_2.max_speed_hz = spi_max_speed

def setOutput(val,xoy):
    # lowbyte has 8 data bits
    # B7, B6, B5, B4, B3, B2, B1, B0
    # D7, D6, D5, D4, D3, D2, D1, D0
    lowByte = val & 0b11111111
    # highbyte has control and 4 data bits
    # control bits are:
    # B7, B6,   B5, B4,     B3,  B2,  B1,  B0
    # W  ,BUF, !GA, !SHDN,  D11, D10, D9,  D8
    # B7=0:write to DAC, B6=0:unbuffered, B5=2:Gain=1X, B4=1:Output is active
    highByte = ((val >> 8) & 0xff) | 0b0 << 7 | 0b0 << 6 | 0b1 << 5 | 0b1 << 4
    #
    # by using spi.xfer2(), the CS is released after each block, transferring the
    # value to the output pin.
    if xoy == 'x':
        spi_1.xfer2([highByte, lowByte])
    elif xoy == 'y':
        spi_2.xfer2([highByte, lowByte])
#=======================Data Acquisition=====================================#
try:
    phase = np.pi/10 #This helps make the Lissajous curves
    while True:
        for angle in np.linspace(0,360,10000000): #lots of data points and 
            angle = angle * ((2 * np.pi) / 360) #high fequency is good for DAC
            
            val_x = .5*np.sin(100000*angle)
            val_x = int((val_x + 1 ) * 2**N / 8)
            setOutput(val_x,'x') #x values
            
            val_y = .5*np.sin(100000*angle*phase)**2
            val_y = int((val_y + 1 ) * 2**N / 8)
            setOutput(val_y,'y') #y values
#===================Get the hell outta dodge=================================#
except KeyboardInterrupt:
    print("Closing SPI channel")
    spi_1.close()
    spi_2.close()
    GPIO.cleanup()
