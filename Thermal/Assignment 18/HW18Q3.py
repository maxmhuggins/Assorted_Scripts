# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:02:52 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt


def heat(T):
    return np.exp(-T**(-1)) / T**2
    
T_vals = np.linspace(0,10,1000)

plt.figure(figsize=(20,10))
plt.plot(T_vals, heat(T_vals))

plt.xlabel('Temperature (K)', fontsize='14')
plt.ylabel('Heat Capacity', fontsize='14')

plt.savefig('H18 Q3.jpg')