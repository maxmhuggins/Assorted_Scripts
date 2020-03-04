# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:12:39 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

energies = [1203.7,965.6,632.4,172]

v_1 = np.linspace(.5, len(energies) - 1 + .5,len(energies))
v = np.linspace(0,9/2, 19)

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