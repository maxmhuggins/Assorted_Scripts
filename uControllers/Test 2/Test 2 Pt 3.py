import RPi.GPIO as GPIO
import time

IR_1 = 33
IR_2 = 36
IR_3 = 32
IR_4 = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_1,GPIO.IN)
GPIO.setup(IR_2,GPIO.IN)
GPIO.setup(IR_3,GPIO.IN)
GPIO.setup(IR_4,GPIO.IN)

try:
    while True:
        ONE = GPIO.input(IR_1)
        TWO = GPIO.input(IR_2)
        THREE = GPIO.input(IR_3)
        FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == False and FOUR == False:
            print('0-22.5 Region')
            while ONE == False and TWO == False and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == False and FOUR == True:
            print('22.5-45 Region')
            while ONE == False and TWO == False and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == True and FOUR == True:
            print('45-67.5 Region')
            while ONE == False and TWO == False and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == True and FOUR == False:
            print('67.5-90 Region')
            while ONE == False and TWO == False and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == True and FOUR == False:
            print('90-112.5 Region')
            while ONE == False and TWO == True and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == True and FOUR == True:
            print('112.5-135 Region')
            while ONE == False and TWO == True and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == False and FOUR == True:
            print('135-157.5 Region')
            while ONE == False and TWO == True and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == False and FOUR == False:
            print('157.5-180 Region')
            while ONE == False and TWO == True and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == False and FOUR == False:
            print('180-202.5 Region')
            while ONE == True and TWO == True and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == False and FOUR == True:
            print('202.5-225 Region')
            while ONE == True and TWO == True and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == True and FOUR == True:
            print('225-247.5 Region')
            while ONE == True and TWO == True and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == True and FOUR == False:
            print('247.5-270 Region')
            while ONE == True and TWO == True and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == True and FOUR == False:
            print('270-292.5 Region')
            while ONE == True and TWO == False and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == True and FOUR == True:
            print('292.5-315 Region')
            while ONE == True and TWO == False and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == False and FOUR == True:
            print('315-332.5 Region')
            while ONE == True and TWO == False and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == False and FOUR == False:
            print('332.5-360 Region')
            while ONE == True and TWO == False and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
                
except KeyboardInterrupt:
    print('toast got burnt')
    
finally:
    print('clean')
    GPIO.cleanup()
