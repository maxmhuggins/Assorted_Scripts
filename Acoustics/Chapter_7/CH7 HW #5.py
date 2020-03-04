# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 03:00:36 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np
#Constants
k = 50*600*10**(-7)
L = 2
R = .5
#Pressure Response
def B(z):
    num = z + L
    den = ((z + L)**2 + R**2)**(1/2)
    other = z/(z**2 + R**2)**(1/2)
    return k*((num / den) - (other))
#a/r values
z = np.linspace(0,5,10000)
#Plotting
fig = plt.figure(1,figsize=(10, 5))
my_fig = fig.add_subplot(111)
my_fig.plot(z, B(z), color = 'b')
my_fig.set_xlabel('$Distance$')
my_fig.set_ylabel('$B-field$')
my_fig.set_title('B vs Distance')
my_fig.set_ylim(ymin=0)
my_fig.set_xlim(xmin=0)
plt.savefig('Q4.png', dpi=300)
