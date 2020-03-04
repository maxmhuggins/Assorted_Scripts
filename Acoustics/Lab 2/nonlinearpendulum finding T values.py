# -*- coding: utf-8 -*-
"""
created on mon sep 24 22:01:10 2018

@author: chris
"""
import matplotlib.pyplot as plt
import numpy as np

l = 1.0
g = 9.8
theta_0 = 1.5708
omega_0 = 0
t_0 = 0 

delta_t = 10**(-2)

theta_values = []
omega_values = []
time_values = []
t2_values = []

theta_values.append(theta_0)
omega_values.append(omega_0)
time_values.append(t_0)

t_i = t_0
omega_i = omega_0
theta_i = theta_0

while omega_i <= 0:
    omega_f = omega_i - (g/l) *np.sin(theta_i) * delta_t
    theta_f = theta_i + omega_f*delta_t
    t_f = t_i + delta_t
    
    theta_values.append(theta_f)
    omega_values.append(omega_f)
    time_values.append(t_f)
    
    omega_i = omega_f
    theta_i = theta_f
    t_i = t_f
        
print(time_values)
print(omega_values)
    
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)

plt.plot(time_values, theta_values, color = 'black', label ='$\\theta_0 = 5\pi/12$ (rad)', linestyle = '-')

my_fig.set_xlabel('$t$ (s)')
my_fig.set_ylabel('$\theta$ (rad)')
my_fig.set_title('nonlinear pendulum')
plt.legend(loc = 'lower right')

plt.savefig('nonlinear_pendulum.png', dpi=300)





