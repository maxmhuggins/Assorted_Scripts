# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:19:28 2019

@author: maxhu
"""
import matplotlib.pyplot as plt

pH = [6.8,6.6,7]
rate = [6.00E-07, 6.19E-07, 1.14E-06]
plt.ylim(5.5e-7, 1.5e-6)
plt.scatter(pH, rate)