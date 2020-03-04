# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:03:19 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

# constants
L = 1.0
g = 9.8
theta_0 = 90*np.pi/180
omega_0 = 0
t_0 = 0 
delta_t = 10**(-3)

# lists to store data
l = np.linspace(0.1,L,1000)
T_values = []
T2_values = []


# nested loop
# for loop handles different lengths of pendulum
for n in range(len(l)):
    # set initial conditions for looping calculations
    flag = True
    t_i = t_0
    omega_i = omega_0
    theta_i = theta_0
    counter = 0
    
    # while loop handles omega and theta values
    while flag == True:
        omega_f = omega_i - (g/l[n]) *np.sin(theta_i) * delta_t
        theta_f = theta_i + omega_f*delta_t
        t_f = t_i + delta_t
        
        omega_i = omega_f
        theta_i = theta_f
        t_i = t_f
        
        # when your current position is really close to the starting position
        # exit the while loop becuase you've gone a full period
        if (np.abs(theta_i - theta_0) < 10**(-3) and counter >= 30):
            flag = False
        
        counter = counter + 1
      
    
    T_values.append(t_i)
    T2_values.append( T_values[n]**2 )
    
    
    
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)
plt.grid(True)
plt.plot(l, T2_values, color = 'black', label ='$\\theta_0 = 5 \degree$', linestyle = '-')

my_fig.set_xlabel('Length of String (m)')
my_fig.set_ylabel('$T^2 (s^2)$')
my_fig.set_title('Nonlinear Pendulum')
plt.legend(loc = 'best')

plt.savefig('nonlinear_pendulum.png', dpi=300)
        
        
        
        
        
        
        