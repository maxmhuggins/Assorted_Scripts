# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:03:36 2020

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

R = .08205
T = 295

def P_fit_p(x, B, C):
    c_1 = (C * x**3) / (R**2 * T**2)
    c_2 = (B * x**2) / (R * T)
    c_3 = (x - 1)
    return (-c_2 + np.sqrt(c_2**2 - 4 * c_1 * c_3)) / (2 * c_1)

def P_fit_m(x, B, C):
    c_1 = (C * x**3) / (R**2 * T**2)
    c_2 = (B * x**2) / (R * T)
    c_3 = (x - 1)
    return (-c_2 - np.sqrt(c_2**2 - 4 * c_1 * c_3)) / (2 * c_1)

Z = [0.9923, 0.9607, 0.9186, 0.8731, 0.8232, 0.7672, 0.7020]

Z_inv = []

for i in Z:
    Z_inv.append(1/i)

P = [.1, .5, 1.0, 1.5, 2.0, 2.5, 3.0]

Z_fit = np.linspace(Z_inv[0],Z_inv[len(Z_inv)-1], 100)
P_fit = np.linspace(.1,3, 100)
    
popt, pcov = curve_fit(P_fit_p, Z_inv, P, bounds=(0,10))
popt
plt.plot(Z_fit, P_fit_p(Z_fit, *popt), label = 'fit')

print(*popt)

plt.plot(Z_inv, P, label = 'data')
plt.legend(loc=('best'))
plt.savefig('HW_1_Q_9.png')

#=======This is obviously no good...=======#