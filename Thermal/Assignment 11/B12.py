# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:07:04 2019

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np
#=========================================#

def REG(x,n):
    return (x**n) * np.exp(-x)
#=========================================#
def GAUSS(x,n):
    y = x - n
    return (n**n) * np.exp(-n) * np.exp((-y**2) / (2 * n))
#=========================================#
x_vals = np.linspace(0,150,1000)
#=========================================#
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(2,2,1)
fig.suptitle('Regular and Gaussian Approximation', fontsize=16)

plt.plot(x_vals, REG(x_vals, 10), label = 'n = 10', color = 'b')
plt.plot(x_vals, GAUSS(x_vals, 10), label = 'n = 10 (Approximation)', color = 'b', linestyle = '--')
plt.legend(loc = 'best')

ax = fig.add_subplot(2,2,2)
plt.plot(x_vals, REG(x_vals, 20), label = 'n = 20', color = 'r')
plt.plot(x_vals, GAUSS(x_vals, 20), label = 'n = 20(Approximation)', color = 'r', linestyle = '--')
plt.legend(loc = 'best')

ax = fig.add_subplot(2,2,3)
plt.plot(x_vals, REG(x_vals, 50), label = 'n = 50', color = 'g')
plt.plot(x_vals, GAUSS(x_vals, 50), label = 'n = 50(Approximation)', color = 'g', linestyle = '--')
plt.legend(loc = 'best')

ax = fig.add_subplot(2,2,4)
plt.plot(x_vals, REG(x_vals, 100), label = 'n = 100', color = 'm')
plt.plot(x_vals, GAUSS(x_vals, 100), label = 'n = 100(Approximation)', color = 'm', linestyle = '--')
plt.legend(loc = 'best')

plt.legend(loc = 'best')
plt.savefig('B11.png', format='png')
