# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:51:48 2019

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

#constants
a = 2
A = 2
ko = 4

def psi(x,a,A):
    return A * np.exp(-2 * a * x**2)

def four(k,a,A,ko):
    return (A * np.exp(-((k - ko)**2)/(4 * a)) * np.sqrt(np.pi / a)) * (1/np.sqrt(2 * np.pi)) 
x_start = -3
x_end = 3
num = 2000

x = np.linspace(x_start,x_end,num)
k = np.linspace(-10,10,2000)

fig = plt.figure(1,figsize=(20,10))
my_fig = fig.add_subplot(1,2,1)
plt.plot(x, psi(x,2,2), color='black', label='$A = 2, a = 2$', linestyle = '-')
plt.legend(loc='upper right')

plt.subplot(1,2,2)
plt.plot(k, four(k,2,2,2), color='black', label='$A = 2, a = 2, k = 2$', linestyle = '-')
plt.legend(loc='upper right')
plt.savefig('A9.png', dpi=300)
