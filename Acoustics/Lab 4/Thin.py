# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 20:37:34 2018

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:28:59 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np


v2_vals = [6890.437,9010.897,11869.85,14362.52,17249.04]
T_vals = [9.610664,14.510664,19.410664,24.310664,29.210664]

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

x_plot = np.arange(6000,20000)
plt.ylim(9,30)

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(v2_vals,T_vals, color = 'g', label = 'Thin String: $m/L = .00188 kg/m$', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('$v^2$ $(m^2/s^2)$')
my_fig.set_ylabel('$T$ (N)')
my_fig.set_title('$T$ vs $v^2$')
plt.legend(loc='best')
plt.savefig('Thinner Guage String.png', dpi=300)