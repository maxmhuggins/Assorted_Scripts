# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:24:10 2020

@author: maxhu
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('classic')

d = 1.53
MM_CO2 = 44.01e-3
MM_N2 = 14.0067e-3
MM_He = 4.0026e-3


CO2_Freq = [1524.390244, 1623.376623, 1666.666667, 1766.784452, 1872.659176, 1923.076923, 2040.816327]
CO2_n_values = [33, 36, 37, 39, 41, 42, 45]
plt.scatter(CO2_n_values, CO2_Freq)

N2_Freq = [1930.501931, 1872.659176, 1689.189189, 1628.664495, 1515.151515, 1400.560224]
N2_n_values = [34, 33, 29, 28, 27, 25]
plt.scatter(N2_n_values, N2_Freq)

He_Freq = [1865.671642, 2136.752137, 1968.503937]
He_n_values = [12, 14, 13]
plt.scatter(He_n_values, He_Freq)

def LinearRegression(x,y, GasName):
    x = np.array(x)
    y = np.array(y)
    m, b, r_value, p_value, std_err = stats.linregress(
            x,y)
    slope=round(m,6)
    c = 2*d*slope
    print('The speed of sound of {} is {}'.format(GasName, round(c,2)))
    if GasName == 'CO2':
        gamma = (MM_CO2*c**2) / (8.314 * 298.15)
    elif GasName == 'N2':
        gamma = (MM_N2*c**2) / (8.314 * 298.15)
    elif GasName == 'He':
        gamma = (MM_He*c**2) / (8.314 * 298.15)
    print('The heat capacity ratio for {} is {}'.format(GasName, round(gamma,3)))
    
    return m*x + b

size = 20
size_config = .8
fig = plt.figure(1,figsize=(10,6))
my_fig = fig.add_subplot(111)
fig.suptitle('$Frequency\ Plotted\ against\ n\ Values$', fontsize=size)
plt.ylabel('$Frequency\ (1/s)$', fontsize=size_config*size)
plt.xlabel('$n$', fontsize=size_config*size)
#=========================================================#
plt.plot(CO2_n_values, LinearRegression(CO2_n_values, CO2_Freq, 'CO2'), 
         color='black', label='$CO_2\ Fit$', linestyle='dotted')
plt.scatter(CO2_n_values, CO2_Freq,color='black', label='$CO_2\ Data$', 
            marker ='+')
#=========================================================#
plt.plot(N2_n_values, LinearRegression(N2_n_values, N2_Freq, 'N2'), 
         color='black', label='$N_2\ Fit$', linestyle='dashed')
plt.scatter(N2_n_values, N2_Freq,color='black', label='$N_2\ Data$', 
            marker ='H')
#=========================================================#
plt.plot(He_n_values, LinearRegression(He_n_values, He_Freq, 'He'), 
         color='black', label='$He\ Fit$', linestyle='dashdot')
plt.scatter(He_n_values, He_Freq,color='black', label='$He\ Data$', 
            marker ='x')
#=========================================================#
plt.legend(loc='best')
plt.savefig('Speed_o_sound.eps')

