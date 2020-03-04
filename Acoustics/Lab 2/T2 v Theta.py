# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:50:43 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np


T2_Theta_vals = [4.13,4.27,4.22,4.05,4.35,4.41,4.50,4.73,5.03,5.09]
Theta_vals = [5*np.pi/180,10*np.pi/180,20*np.pi/180,30*np.pi/180,40*np.pi/180,50*np.pi/180,60*np.pi/180,70*np.pi/180,80*np.pi/180,90*np.pi/180]

N = len(Theta_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T2_Theta_vals[i]
    sum_x = sum_x + Theta_vals[i]
    sum_xy = sum_xy + Theta_vals[i]*T2_Theta_vals[i]
    sum_x_squared = sum_x_squared + Theta_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T2_Theta_vals[i] - A - B*Theta_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

x_plot = np.arange(0,90*np.pi/180)
plt.ylim((3.5,5.5))

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(Theta_vals,T2_Theta_vals, color = 'b', label = 'Experimental Data', marker='o')
#plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
#plt.legend(loc = 'best')


L = 1.0
g = 9.8
theta_min = 5*np.pi/180
theta_max = np.pi/2
omega_0 = 0
t_0 = 0 
delta_t = 10**(-4)

# lists to store data
thetas = np.linspace(theta_min, theta_max, 100)
T_values = []
T2_values = []


# nested loop
# for loop handles different lengths of pendulum
for n in range(len(thetas)):
    # set initial conditions for looping calculations
    flag = True
    t_i = t_0
    omega_i = omega_0
    theta_i = thetas[n]
    counter = 0
    
    # while loop handles omega and theta values
    while flag == True:
        omega_f = omega_i - (g/L) *np.sin(theta_i) * delta_t
        theta_f = theta_i + omega_f*delta_t
        t_f = t_i + delta_t
        
        omega_i = omega_f
        theta_i = theta_f
        t_i = t_f
        
        # when your current position is really close to the starting position
        # exit the while loop becuase you've gone a full period
        if (np.abs(theta_i - thetas[n]) < 10**(-4) and counter >= 300):
            flag = False
        
        counter = counter + 1
      
    
    T_values.append(t_i)
    T2_values.append( T_values[n]**2 )
    
    
    
fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)
plt.grid(True)
plt.plot(thetas, T2_values, color = 'g', label ='Nonlinear Model', linestyle = '-.')

my_fig.set_xlabel('Starting Angle (rad)')
my_fig.set_ylabel('$T^2 (s^2)$')
my_fig.set_title('$T^2$ vs Varied Starting Angles')
plt.legend(loc = 'best')

T2_linear_Theta_vals = [4.02,4.02,4.02,4.02,4.02,4.02,4.02,4.02,4.02,4.02]

N = len(Theta_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T2_linear_Theta_vals[i]
    sum_x = sum_x + Theta_vals[i]
    sum_xy = sum_xy + Theta_vals[i]*T2_linear_Theta_vals[i]
    sum_x_squared = sum_x_squared + Theta_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T2_linear_Theta_vals[i] - A - B*Theta_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

x_plot = np.linspace(0,90*np.pi/180,11)
plt.ylim((3.8,5.25))

def my_fit(x):
    return (A + B*x)

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig2 = fig.add_subplot(1,1,1)
my_fig.grid(True)
#my_fig.scatter(Theta_vals, T2_linear_Theta_vals, color = 'red', label = 'Linear Model', marker='v')
my_fig2.plot(x_plot,my_fit(x_plot), color ='red', label = 'Linear Model', linestyle = '--')
plt.legend(loc = 'best')
plt.savefig('T2 v Theta.png', dpi=300)
