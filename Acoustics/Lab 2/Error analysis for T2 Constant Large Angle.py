# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:30:47 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np


T2_vals = [4.99,4.31,3.98,3.32,2.93,2.41,1.86,1.48,1.01,0.49]
L_vals = [1,.9,.8,.7,.6,.5,.4,.3,.2,.1]

N = len(L_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T2_vals[i]
    sum_x = sum_x + L_vals[i]
    sum_xy = sum_xy + L_vals[i]*T2_vals[i]
    sum_x_squared = sum_x_squared + L_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T2_vals[i] - A - B*L_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

x_plot = np.arange(0,1.1)
plt.ylim(.35,5.1)

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(L_vals,T2_vals, color = 'g', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('Mass (g)')
my_fig.set_ylabel('$T^2/4\pi^2$')
my_fig.set_title('$T^2/4\pi^2$ vs Mass No Speaker Box')
plt.savefig('Err in T2 Large Angle.png', dpi=300)
