# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:46:37 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

def C(t):
    first = 1 / t**2
    second = np.exp(1/t) / (np.exp(1/t) - 1)**2
    return first * second

t = np.linspace(0,2,100)
plt.figure(figsize=(15,10))
plt.plot(t, C(t))
plt.xlabel('$kT/\epsilon$')
plt.ylabel('$C/Nk$')
plt.title('Heat Capacity of an E.S. Relative to Temp')

plt.savefig('HW21Q2')