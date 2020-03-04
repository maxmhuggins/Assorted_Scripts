# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 03:21:34 2019

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

N = 0

def Ohm(z,N):
    return (4 * z * (1 - z))**N
    
x = np.linspace(0,1,1000000)
fig = plt.figure(figsize = (20, 10))
plt.plot(x, Ohm(x,1), label = '1')
plt.plot(x, Ohm(x,10), label = '10')
plt.plot(x, Ohm(x,100), label = '100')
plt.plot(x, Ohm(x,1000), label = '1000')
plt.plot(x, Ohm(x,10000), label = '10000')

plt.title('$z^N(1-z)^N$ at Different N Values')
plt.legend(loc = 'best')

plt.savefig('MultiplicityQ221.png')

