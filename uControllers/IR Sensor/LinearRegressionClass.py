# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:57:05 2019

@author: maxhu
"""
import numpy as np

def linear_regression(x_values, y_values):
    y_values = []
    x_values = []
#    lines = np.loadtxt('LOADINTEXTFILEHERE.txt', delimiter=',')
#    for line in lines:
#        x_values.append(line[0])
#        y_values.append(line[1])
    N = len(x_values)
    sum_y = 0
    sum_x = 0
    sum_xy = 0
    sum_x_squared = 0
    
    for i in range(0,N):
        sum_y = sum_y + y_values[i]
        sum_x = sum_x + x_values[i]
        sum_xy = sum_xy + x_values[i]*y_values[i]
        sum_x_squared = sum_x_squared + x_values[i]**2
        
    Delta = N*sum_x_squared - (sum_x)**2
    global A
    global B
    A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
    B = (N*sum_xy - sum_x*sum_y) / Delta
    
    deviation = 0
    
    for i in range (0,N):
        deviation = deviation + (y_values[i] - A - B*x_values[i])**2
        
    sigma_y = np.sqrt(deviation / (N-2))
    
    sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
    sigma_B = sigma_y*np.sqrt(N/Delta)
    
    print('The best estimate for A is: ', A)
    print("The best estimate for the uncertainty in A is: ", sigma_A)
    
    print('The best estimate for B is: ', B)
    print("The best estimate for the uncertainty in B is: ", sigma_B)
    return B

def my_fit(x):#Plot this in your figure for linear regression line
    return A + B*x