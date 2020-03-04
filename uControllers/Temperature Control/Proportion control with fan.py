# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:01:18 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

time_data1 = []
temp_data1 = []

time_data2 = []
temp_data2 = []

time_data3 = []
temp_data3 = []

for i in range(1,4):
    lines = np.loadtxt('./Data/TempProcessControl{}.txt'.format(i), delimiter=',')
    for line in lines:
        if i == 1:       
            time_data1.append(line[0])
            temp_data1.append(line[1])
        elif i == 2:
            time_data2.append(line[0])
            temp_data2.append(line[1])
        elif i == 3:
            time_data3.append(line[0])
            temp_data3.append(line[1])

plt.figure(figsize=(10,10))
#plt.plot(time_data,temp_data, 'm')
#plt.scatter(time_data1,temp_data1, s = 5, color = 'm', label = 'Active Cooling')
#plt.scatter(time_data2,temp_data2, s = 5, color = 'g', label = 'Bang Bang')
#plt.scatter(time_data3,temp_data3, s = 5, label = 'No cooling')

plt.plot(time_data1,temp_data1, color = 'm', label = 'Active Cooling')
plt.plot(time_data2,temp_data2, color = 'g', label = 'Bang Bang')
plt.plot(time_data3,temp_data3, label = 'No cooling')

plt.plot(np.linspace(0,1800),np.linspace(30,30), color = 'r', label = r'29$\degree$ and 31$\degree$ mark')
#plt.plot(np.linspace(0,1800),np.linspace(31,31), color = 'r')
plt.legend(loc='best')


plt.ylim(10,90)