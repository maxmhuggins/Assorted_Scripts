# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:48:10 2018

@author: maxhu
"""


import matplotlib.pyplot as plt
import numpy as np

m_vals = [0, 5, 10, 15, 20, 25, 30]
T24pi2_bf_vals = [3.903108543E-06, 4.605458805E-06, 4.959850988E-06, 5.699398775E-06, 6.348140877E-06, 7.019913626E-06, 7.971177951E-06]

N = len(m_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + T24pi2_bf_vals[i]
    sum_x = sum_x + m_vals[i]
    sum_xy = sum_xy + m_vals[i]*T24pi2_bf_vals[i]
    sum_x_squared = sum_x_squared + m_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (T24pi2_bf_vals[i] - A - B*m_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

x_plot = np.arange(0,35)
plt.ylim((3.5E-06,8.5E-06))

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(m_vals,T24pi2_bf_vals, color = 'g', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('Mass (g)')
my_fig.set_ylabel('$T^2/4\pi^2$')
my_fig.set_title('$T^2/4\pi^2$ vs Mass With Speaker Box, No Foam')
plt.savefig('box with foam.png', dpi=300)
