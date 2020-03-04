# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 00:23:38 2020

@author: maxhu
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

R = 8.314
T = 295

def P_fit(Z, B, C):
    a = C / (R*T)**2
    b = (B*Z)/(R*T)
    c = Z**2-Z**3
    return (-b+np.sqrt(b**2-4*a*c))/(2*a)

Z = [0.9923, 0.9607, 0.9186, 0.8731, 0.8232, 0.7672, 0.7020]

Z_inv = []

for i in Z:
    Z_inv.append(1/i)

P = [.1e6, .5e6, 1.0e6, 1.5e6, 2.0e6, 2.5e6, 3.0e6]

Z_fit = np.linspace(Z_inv[0],Z_inv[len(Z_inv)-1], 100)
    
popt, pcov = curve_fit(P_fit, Z_inv, P, bounds=(0,100))
popt
plt.plot(Z_fit, P_fit(Z_fit, *popt), label = 'fit')

print(*popt)

plt.plot(Z_inv, P, label = 'data')
plt.legend(loc=('best'))
plt.savefig('HW_1_Q_9.png')
