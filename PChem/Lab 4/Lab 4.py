# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:38:30 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

A_1 = []
l_1 = []

A_2 = []
l_2 = []

A_3 = []
l_3 = []


lines = np.loadtxt('first_column.txt')
for line in lines:
    l_1.append(line[0])
    A_1.append(line[1])
    
lines = np.loadtxt('second_column.txt')
for line in lines:
    l_2.append(line[0])
    A_2.append(line[1])
    
lines = np.loadtxt('third_column.txt')
for line in lines:
    l_3.append(line[0])
    A_3.append(line[1])

fig = plt.figure(1,figsize=(15, 10))
my_fig = fig.add_subplot(111)
my_fig.set_title('Absorbance versus Wavelength', fontsize = '15')

plt.plot(l_1,A_1, color='black', label="1,1' diethyl-2,2' cyanine iodide")
plt.plot(l_2,A_2, color='c', label="1,1' diethyl-2,2' carbocyanine iodide")
plt.plot(l_3,A_3, color='m', label="1,1' diethyl 4,4' dicarbocyanine iodide")


my_fig.set_xlabel('$\lambda$(nm)', fontsize = '13')
my_fig.set_ylabel('A', fontsize = '13')

plt.legend(loc='best', fontsize = '13')
plt.savefig('All_three.png', dpi=900)
