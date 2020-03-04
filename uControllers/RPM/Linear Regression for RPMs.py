# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:03:28 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

RPMs = []
duty_cycles = []


lines = np.loadtxt('RPMs9.txt', delimiter=',')
for line in lines:
    RPMs.append(line[1])
    duty_cycles.append(line[0])

N = len(duty_cycles)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + RPMs[i]
    sum_x = sum_x + duty_cycles[i]
    sum_xy = sum_xy + duty_cycles[i]*RPMs[i]
    sum_x_squared = sum_x_squared + duty_cycles[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0

for i in range (0,N):
    deviation = deviation + (RPMs[i] - A - B*duty_cycles[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

def my_fit(x):#Plot this in your figure for linear regression line
    return A + B*x
fig = plt.figure(figsize=(20,10))
plt.scatter(duty_cycles,RPMs)
plt.plot(duty_cycles,RPMs, 'm', label = 'Pause time = 8s')
plt.xlabel('Duty cycles')
plt.legend(loc='best')
plt.savefig('RPMvDuty.png')




