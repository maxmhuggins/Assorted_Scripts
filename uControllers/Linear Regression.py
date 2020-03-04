# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:51:42 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

TEMPS = []
TIMES = []

lines = np.loadtxt('BangBangControl.txt', delimiter=',')
for line in lines:
    TIMES.append(line[0])
    TEMPS.append(line[1])

N = len(TIMES)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + TEMPS[i]
    sum_x = sum_x + TIMES[i]
    sum_xy = sum_xy + TIMES[i]*TEMPS[i]
    sum_x_squared = sum_x_squared + TIMES[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0

for i in range (0,N):
    deviation = deviation + (TEMPS[i] - A - B*TIMES[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

def my_fit(x):#Plot this in your figure for linear regression line
    return A + B*x
plt.figure(figsize=(40,20))
plt.scatter(TIMES,TEMPS, s= 1)
plt.plot(TIMES,TEMPS, color = 'black')