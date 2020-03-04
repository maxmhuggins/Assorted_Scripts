# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:51:42 2019

@author: maxhu
"""

import numpy as np

YOUR_Y_VALUES = []
YOUR_X_VALUES = []

N = len(YOUR_X_VALUES)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + YOUR_Y_VALUES[i]
    sum_x = sum_x + YOUR_X_VALUES[i]
    sum_xy = sum_xy + YOUR_X_VALUES[i]*YOUR_Y_VALUES[i]
    sum_x_squared = sum_x_squared + YOUR_X_VALUES[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0

for i in range (0,N):
    deviation = deviation + ('Y DATA ARRAY GOES HERE'[i] - A - B*'X DATA ARRAY GOES HERE'[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

def my_fit(x):#Plot this in your figure for linear regression line
    return A + B*x