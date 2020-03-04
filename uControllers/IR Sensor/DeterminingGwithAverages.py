import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np
import LinearRegressionClass as linreg

y = .050
IR = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR,GPIO.IN)

plot_t = []
avg_v = []
del_t = []
g_values = []

try:
    my_test = True
    count = 0
    while my_test == True:
        count = count + 1
        picket_count = 0
        IR_state = GPIO.input(IR)
        start_total = time.time()
        while picket_count < 7:
            IR_state = GPIO.input(IR)
            if IR_state == False:
                start_t = time.time()
                while IR_state == False:
                    IR_state = GPIO.input(IR)
                    pass
                plot_t.append(time.time() - start_total)
                IR_state = GPIO.input(IR)
                while IR_state == True:
                    IR_state = GPIO.input(IR)
                    pass
                del_t.append(time.time() - start_t)
                picket_count = picket_count + 1

        for i in range(0,7):
            v = (y) / del_t[i]
            avg_v.append(v)
        linreg.linear_regression(plot_t, avg_v)
        g_values.append(B)
        if count > 10:
            g_avg = np.mean(np.array(g_values))
            my_test = False
            print(g_avg)
        
        
except KeyboardInterrupt:
    print("that can't be good...")

finally:
    GPIO.cleanup()
    print('Isaac cleaned the oven.')
