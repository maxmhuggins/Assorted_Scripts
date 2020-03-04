# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 06:50:45 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

def A(x):
    return np.sin(x)

x = np.linspace(0,360,5000)
y = x/2
plt.plot(A(y), A(x), 'm')
plt.savefig('pattern_1digital.png')
y = 2.25*x
plt.plot(A(x), A(y), 'm')
plt.savefig('pattern_3digital.png')