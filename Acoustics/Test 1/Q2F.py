# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 05:38:47 2018

@author: maxhu
"""
#This code doesn't work, unfortunately. I believe the order of my loops 
#is whacky and is causing it to not work properly.
import numpy as np
import math
import matplotlib.pyplot as plt
zero_values = []

def BesselJ(u):
    BJ = 0    
    for i in range (0,100):
        flag = True
        while flag == True:
            for i in range (0,100):
                coeff = ((-1)**i)/(2**(2*i)*math.factorial(i)*math.factorial(i))
                BJ = BJ + coeff*u**(2*i)
                if np.abs(coeff) <= 1:
                    flag = False
                    zero_values.append(u)
            return BJ
                
u_values = np.linspace(0,20,100)
print(zero_values)

fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.plot(u_values,BesselJ(u_values), color = 'black', linestyle = 'solid', label='$n=0$')
my_fig.set_xlabel('$u$')
my_fig.set_ylabel('$J_n(u)$')
my_fig.set_title('Bessel Functions')
plt.legend(loc='upper right')
plt.savefig('Q2EZeroCrossings.png', dpi=300)

      