# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 08:38:43 2018

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
#constants
r1 = 12.9*10**6
r2 = 3.2*10**6
r3 = 1.54*10**6
f = 1
c = 2650
L = .0001

#Define acoustic pressure amplitudes
def T(f):
    first_term = 2+((r3/r1)+(r1/r3))*(np.cos((2*np.pi*f*L)/c))**2
    second_term = ((r2**2/(r1*r3))+((r1*r3)/r2**2))*(np.sin((2*np.pi*f*L)/c))**2
    return 4/(first_term + second_term)
f_values = np.linspace(1*10**6, 50*10**6, 1000000)
#plt.ylim(.89,.91)
#plt.xlim(4.5*10**7, 4.7*10**7)

#Plotting
fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.plot(f_values, T(f_values), color = 'blue')
my_fig.set_xlabel('Frequency (Hz)')
my_fig.set_ylabel('$T_i$')
my_fig.set_title('Ultrasound Transmission intensity at different frequencies')
plt.legend(loc='best')
plt.savefig('Q2PartB.png', dpi=300)
