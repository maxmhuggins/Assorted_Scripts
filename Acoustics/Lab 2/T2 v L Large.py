# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:19:45 2018

@author: maxhu
"""
import matplotlib.pyplot as plt
import numpy as np


T2_large_vals = [4.99,4.31,3.98,3.32,2.93,2.41,1.86,1.48,1.01,.49]
L_large_vals = [1.0,.9,.8,.7,.6,.5,.4,.3,.2,.1]

N = len(L_large_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T2_large_vals[i]
    sum_x = sum_x + L_large_vals[i]
    sum_xy = sum_xy + L_large_vals[i]*T2_large_vals[i]
    sum_x_squared = sum_x_squared + L_large_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T2_large_vals[i] - A - B*L_large_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

x_plot = np.linspace(0,1,11)
plt.ylim((0,5))

def my_fit(x):
    return (A + B*x)

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
my_fig.scatter(L_large_vals, T2_large_vals, color = 'b', label = 'Experimental Data', marker='o')
#my_fig.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('L (m)')
my_fig.set_ylabel('$T^2$ $(s^2)$')
my_fig.set_title('$T^2$ vs L for $90^\circ$ Starting Angle')
plt.legend(loc = 'best')

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
        if (np.abs(theta_i - theta_0) < 10**(-3) and counter >= 25):
            flag = False
        #This counter ensures that the theta goes back to starting position and not just move a small step
        counter = counter + 1
      
    
    T_values.append(t_i)
    T2_values.append( T_values[n]**2 )
    
    
    
fig = plt.figure(1)
plt.plot(l, T2_values, color = 'g', label ='Nonlinear Model', linestyle = '-.')


T2_linear_large_vals = [4.02,3.62,3.22,2.82,2.41,2.01,1.61,1.21,.80,.40]
L_small_vals = [1.0,.9,.8,.7,.6,.5,.4,.3,.2,.1]


N = len(L_small_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T2_linear_large_vals[i]
    sum_x = sum_x + L_small_vals[i]
    sum_xy = sum_xy + L_small_vals[i]*T2_linear_large_vals[i]
    sum_x_squared = sum_x_squared + L_small_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T2_linear_large_vals[i] - A - B*L_small_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

x_plot = np.linspace(0,1,11)
plt.ylim((0,5))

def my_fit(x):
    return (A + B*x)

fig = plt.figure(1)

#my_fig.scatter(L_small_vals, T2_linear_large_vals, color = 'red', label = 'Linear Model', marker='v')
my_fig.plot(x_plot,my_fit(x_plot), color ='red', label = 'Linear Model', linestyle = '--')
plt.legend(loc = 'best')
plt.savefig('T2 v L Large.png', dpi=300)
