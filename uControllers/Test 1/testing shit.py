# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:45:21 2019

@author: maxhu
"""

import numpy as np
#define data arrays
time_data = []
voltage_data = []
R_1 = 100
R_2 = 100
lines = np.loadtxt('Test_1.txt', delimiter=',')
for line in lines:
    time_data.append(line[0] / 3600)
    v_in = ((R_1 + R_2) / (R_1)) * line[1]
    voltage_data.append(v_in)

print(time_data)
print(voltage_data)