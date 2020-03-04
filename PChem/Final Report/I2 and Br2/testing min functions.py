# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:05:52 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10, 21)

y = x**2

plt.plot(x, y)

minima = []

for i in range(1,len(x)-1):
    down = y[i-1] - y[i]
    up = y[i+1] - y[i]
    if up > 0 and down > 0:
        minima.append(x[i])
        print(i)
        
print(minima)