import RPi.GPIO as GPIO
import time

IR_1 = 36
IR_2 = 32
IR_3 = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_1,GPIO.IN)
GPIO.setup(IR_2,GPIO.IN)
GPIO.setup(IR_3,GPIO.IN)

try:
    while True:
        ONE = GPIO.input(IR_1)
        TWO = GPIO.input(IR_2)
        THREE = GPIO.input(IR_3)
        if ONE == False and TWO == False and THREE == False:
            print('0-45 Region')
        if ONE == False and TWO == False and THREE == True:
            print('45-90 Region')
        if ONE == False and TWO == True and THREE == True:
            print('90-135 Region')
        if ONE == False and TWO == True and THREE == False:
            print('135-180 Region')
        if ONE == True and TWO == True and THREE == False:
            print('180-225 Region')
        if ONE == True and TWO == True and THREE == True:
            print('225-270 Region')
        if ONE == True and TWO == False and THREE == True:
            print('270-315 Region')
        if ONE == True and TWO == False and THREE == False:
            print('315-360 Region')

except KeyboardInterrupt:
    print('toast got burnt')
    
finally:
    print('clean')
    GPIO.cleanup()
