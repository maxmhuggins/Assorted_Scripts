# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 05:15:49 2018

@author: maxhu
"""
#Question 2 Part E
import numpy as np
import math
import matplotlib.pyplot as plt

def BesselJ(n,u):
    BJ = 0
    for i in range (0,100):
        coeff = ((-1)**i)/(2**(2*i+n)*math.factorial(i)*math.factorial(n+i))
        BJ = BJ + coeff*u**(2*i+n)
    return BJ

u_values = np.linspace(0,20,100)

fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.plot(u_values,BesselJ(0,u_values), color = 'black', linestyle = 'solid', label='$n=0$')
plt.plot(u_values,BesselJ(1,u_values), color = 'black', linestyle = 'dashed', label='$n=1$')
plt.plot(u_values,BesselJ(2,u_values), color = 'black', linestyle = 'dotted', label='$n=2$')
my_fig.set_xlabel('$u$')
my_fig.set_ylabel('$J_n(u)$')
my_fig.set_title('Bessel Functions')
plt.legend(loc='upper right')
plt.savefig('Q2EBesselFunctions.png', dpi=300)

      