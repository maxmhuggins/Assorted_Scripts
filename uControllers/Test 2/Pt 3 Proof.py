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
    sector = []
    while len(sector) < 33:
        ONE = GPIO.input(IR_1)
        TWO = GPIO.input(IR_2)
        THREE = GPIO.input(IR_3)
        FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == False and FOUR == False:
            sector.append('1')
            while ONE == False and TWO == False and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == False and FOUR == True:
            sector.append('2')
            while ONE == False and TWO == False and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == True and FOUR == True:
            sector.append('3')
            while ONE == False and TWO == False and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == False and THREE == True and FOUR == False:
            sector.append('4')
            while ONE == False and TWO == False and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == True and FOUR == False:
            sector.append('5')
            while ONE == False and TWO == True and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == True and FOUR == True:
            sector.append('6')
            while ONE == False and TWO == True and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == False and FOUR == True:
            sector.append('7')
            while ONE == False and TWO == True and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == False and TWO == True and THREE == False and FOUR == False:
            sector.append('8')
            while ONE == False and TWO == True and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == False and FOUR == False:
            sector.append('9')
            while ONE == True and TWO == True and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == False and FOUR == True:
            sector.append('10')
            while ONE == True and TWO == True and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == True and FOUR == True:
            sector.append('11')
            while ONE == True and TWO == True and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == True and THREE == True and FOUR == False:
            sector.append('12')
            while ONE == True and TWO == True and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == True and FOUR == False:
            sector.append('13')
            while ONE == True and TWO == False and THREE == True and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == True and FOUR == True:
            sector.append('14')
            while ONE == True and TWO == False and THREE == True and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == False and FOUR == True:
            sector.append('15')
            while ONE == True and TWO == False and THREE == False and FOUR == True:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
        if ONE == True and TWO == False and THREE == False and FOUR == False:
            sector.append('16')
            while ONE == True and TWO == False and THREE == False and FOUR == False:
                ONE = GPIO.input(IR_1)
                TWO = GPIO.input(IR_2)
                THREE = GPIO.input(IR_3)
                FOUR = GPIO.input(IR_4)
    file = open('Pt3.txt', 'w')
    for n in range(len(sector)):
        file.write(str(sector[n]) + ',')
    file.close()

                
except KeyboardInterrupt:
    print('toast got burnt')
    
finally:
    print('clean')
    GPIO.cleanup()
