import RPi.GPIO as GPIO
import time

IR = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR,GPIO.IN)

try:
    my_test = True
    start_time = time.time()
    while my_test == True:
        picket_count = 0
        while picket_count < 8:
            IR_state = GPIO.input(IR)
            if IR_state == False:
                while IR_state == False:
                    IR_state = GPIO.input(IR)
                    pass
                picket_count = picket_count + 1
                
        print(picket_count)
        
except KeyboardInterrupt:
    print("that can't be good...")

finally:
    GPIO.cleanup()
    print('Isaac cleaned the oven.')
