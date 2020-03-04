# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:24:06 2019

@author: maxhu
"""

import numpy as np

R_1 = 98.5
R_2 = 98.4

#define data arrays
time_data = []
voltage_data = []
current_data = []
SUM = 0


#read in data
lines = np.loadtxt('Test1NEWCode.txt', delimiter=',')
for line in lines:
    time_data.append(line[0] / 3600)
    v_in = ((R_1 + R_2) / (R_1)) * line[1]
    voltage_data.append(v_in)
    
for n in range(len(voltage_data)):
    I_o = voltage_data[n] / (R_1 + R_2)
    I_f = round(I_o,3)
    current_data.append(I_f)

for n in range(1, len(time_data)):
    A_n = .5 * (current_data[n] + current_data[n-1]) * (np.abs(time_data[n-1] - time_data[n]))
    SUM = SUM + A_n
print(np.average(current_data))
print('The total amp-hours of your battery is:', round(SUM,3), 'Ah')