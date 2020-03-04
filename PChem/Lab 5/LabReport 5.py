# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:31:38 2019

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

wavelengths = [656.3, 486.1, 434, 410.2, 397, 388.9, 383.5, 379.8]
x = np.linspace(700,350, 100)

function = []

for i in x:
    for l in wavelengths:
        if l - i < .001:
            function.append(1)
            break
    function.append(0)

plt.plot(x, function)