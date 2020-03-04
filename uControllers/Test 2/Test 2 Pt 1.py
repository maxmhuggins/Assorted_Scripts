import RPi.GPIO as GPIO
import time

IR_1 = 36
IR_2 = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_1,GPIO.IN)
GPIO.setup(IR_2,GPIO.IN)

try:
    while True:
        ONE = GPIO.input(IR_1)
        TWO = GPIO.input(IR_2)
        if ONE == False and TWO == False:
            ONE = GPIO.input(IR_1)
            TWO = GPIO.input(IR_2)
            if ONE == True:
                print('CC')
            elif TWO == True:
                print('C')
                
except KeyboardInterrupt:
    print('toast got burnt')
    
finally:
    print('clean')
    GPIO.cleanup()
