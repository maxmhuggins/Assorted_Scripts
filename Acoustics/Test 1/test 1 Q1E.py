#Question 1 Part E
#For some reason my code is not quite right and all of the waveforms are the
#same just scaled differently at different y/yo values
import matplotlib.pyplot as plt
import numpy as np

v_0 = 0
t_0 = 0
m = 1
delta_t = 10**(-2)
y_0 = 0
k = 9*10**9
q1 = 1*10**-3
q2 = 1*10**-3
m2 = 1
g = 9.8
y_o = np.sqrt((k*q1*q2)/m2*g)
A_0 = 2

y_values = []
v_values = []
time_values = []



y_values.append(y_0)
v_values.append(v_0)
time_values.append(t_0)


t_i = t_0
v_i = v_0
y_i = y_0
v_f = v_0
A_i = A_0

for n in range(10000):
    v_f = g*delta_t*((1/(1+A_i)**2)-1)+v_i
    y_f = y_i + v_f*delta_t
    t_f = t_i + delta_t
    A_f = (y_i + v_f*delta_t)/y_o
    
    y_values.append(y_f)
    v_values.append(v_f)
    time_values.append(t_f)
    
    v_i = v_f
    y_i = y_f
    t_i = t_f
    A_i = A_f
    
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)

plt.plot(time_values, y_values, color = 'black', label ='$Y^\prime(0)/Y_o$ = 2', linestyle = '-')


my_fig.set_xlabel('Time (s)')
my_fig.set_ylabel('Y Displacement (m)')
my_fig.set_title('Displacement vs Time')
plt.legend(loc = 'lower right')

plt.savefig('DisplacementVtime2.png', dpi=300)
