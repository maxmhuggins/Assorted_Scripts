import RPi.GPIO as GPIO
import time

FAN = 12
IR = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR,GPIO.IN)
GPIO.setup(FAN,GPIO.OUT)

freq = 1
lowest_duty = 20
my_pwm = GPIO.PWM(FAN, freq)

duty_cycle = 0
my_pwm.start(duty_cycle)
pause_time = 2

try:
    for p in range(0,21,1):
        RPMs = []
        duty_cycles = []
        my_pwm.ChangeDutyCycle(lowest_duty)
        time.sleep(30)
        for i in range(lowest_duty,101,1):
            revs = 0
            duty_cycle = i
            print('the duty cycle is:', duty_cycle)
            my_pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(p)
            start_time = time.time()
            while revs <= 3000:
                IR_state = GPIO.input(IR)
                if IR_state == False:
                    while IR_state == False:
                        IR_state = GPIO.input(IR)
                        pass
                    revs = revs + 1
            total_time = (time.time() - start_time) / 60
            RPM = (revs / total_time) / 7
            RPMs.append(RPM)
            duty_cycles.append(i)
        print(RPMs)
        file = open('./RPMDATA/RPMs{}.txt'.format(p), 'w')
        for n in range(len(RPMs)):
            #Write the data as comma delimites
            file.write(str(duty_cycles[n]) + ',' + str(RPMs[n]) + '\n')
        #always close the file you are using

        file.close()
        
except KeyboardInterrupt:
    my_pwm.stop()
    print('toast got burnt')
    
finally:
    GPIO.cleanup()
