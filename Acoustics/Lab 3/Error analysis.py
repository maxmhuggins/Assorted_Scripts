# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:28:59 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np


v2_vals = [13668.5915,19114.15974,25079.04132,29865.87459,35852.59924]
T_vals = [38.8849,54.256,70.2351,85.9102,101.585]

N = len(v2_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T_vals[i]
    sum_x = sum_x + v2_vals[i]
    sum_xy = sum_xy + v2_vals[i]*T_vals[i]
    sum_x_squared = sum_x_squared + v2_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T_vals[i] - A - B*v2_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

x_plot = np.arange(13000,40000)
plt.ylim(30,110)

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(v2_vals,T_vals, color = 'g', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('Mass (g)')
my_fig.set_ylabel('$T^2/4\pi^2$')
my_fig.set_title('$T^2/4\pi^2$ vs Mass No Speaker Box')
plt.savefig('mass_spring_example.png', dpi=300)




