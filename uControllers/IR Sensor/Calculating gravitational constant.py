import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np

IR = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR,GPIO.IN)


y = .025

avgs = []
times = []
instant_times = []

try:
    my_test = True
    
    while my_test == True:
        picket_count = 0
        IR_state = GPIO.input(IR)
        first_start = time.time()
        while picket_count < 8:
            IR_state = GPIO.input(IR)
            if IR_state == False:
                start_time = time.time()
                while IR_state == False:
                    IR_state = GPIO.input(IR)
                    pass
                times.append(time.time() - start_time)
                instant_times.append(time.time() - first_start)
                picket_count = picket_count + 1

        for i in range(0,8):
            v_avg = y / times[i]
            v_avg = round(v_avg,3)
            avgs.append(v_avg)
        print(avgs)
        my_test = False
    file = open('g_Constant.txt', 'w')
    for n in range(0,8):
        #Write the data as comma delimites
        file.write(str(instant_times[n]) + ',' + str(avgs[n]) + '\n')
    #always close the file you are using

    file.close()
        
except KeyboardInterrupt:
    print("that can't be good...")

finally:
    GPIO.cleanup()
    print('Isaac cleaned the oven.')
