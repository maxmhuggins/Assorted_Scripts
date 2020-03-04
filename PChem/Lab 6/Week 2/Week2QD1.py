# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:38:28 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

energies = [2191, 2064, 1941, 1821, 1705, 1591, 1479, 1368, 1257, 1145, 1033, 918, 800, 677, 548, 411]

v_1 = np.linspace(.5, 31/2,16)
v = np.linspace(0,39/2, 19)

area = []

slope, intercept, r_value, p_value, std_err = stats.linregress(v_1,energies)
y = slope*v + intercept

for i in range(0,len(v)-1):
    b_1 = y[i]
    b_2 = y[i+1]
    h = v[i+1] - v[i]
    area.append(.5 * (b_1 + b_2) * h)
        
print(sum(area))

plt.scatter(v_1, energies)
plt.plot(v, y)