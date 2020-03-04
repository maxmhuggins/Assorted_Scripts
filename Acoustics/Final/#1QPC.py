# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:48:53 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

#Constants
c = 343
T = 1.7*10**(-10)

#Functions
def cp(f):  #Phase speed
    num = (np.sqrt(1 + ((2 * np.pi * f) * T)**2) + 1)
    den = (1 + ((2 * np.pi * f) * T)**2)
    return c * np.sqrt(2) * np.sqrt( den/num )

def a(f):
    num = (np.sqrt(1 + ((2 * np.pi * f) * T)**2) - 1)
    den = (1 + ((2 * np.pi * f) * T)**2)
    return (2 * np.pi * f) * (1 / f) * np.sqrt(2) * np.sqrt( num/den )

#plotting
f_values = np.linspace(10**6,10**(15),10500000)

fig = plt.figure(1,figsize=(15, 5))
my_fig = fig.add_subplot(121)
plt.loglog(f_values, cp(f_values), color = 'b')
my_fig.set_xlabel('Frequency')
my_fig.set_ylabel('Phase Speed')
my_fig.set_title('Phase Speed by Frequency')

my_fig = fig.add_subplot(122)
plt.loglog(f_values, a(f_values), color = 'green')
my_fig.set_xlabel('Frequency')
my_fig.set_ylabel('Attenuation x Wavelength')
my_fig.set_title('Attenuation times Wavelength by Frequency')
plt.savefig('Q1PC.png', dpi=300)


