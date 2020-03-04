#-*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:22:59 2018

@author: maxhu
"""

import numpy as np
from statistics import mean
import matplotlib.pyplot as plt

#Emperical data from experiment
T24pi2_vals = np.array([1.65854E-05, 1.84218E-05, 1.9895E-05, 2.10582E-05, 2.60478E-05, 2.85528E-05, 3.01498E-05], dtype=np.float64)
m_vals = np.array([0, .005, .010, .015, .020, .025, .030], dtype=np.float64)

#defining variables from experimental data
xs = m_vals
ys = T24pi2_vals

#Making a line of best fit
def best_fit_slope_and_intercept(xs,ys):
    m1 = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b1 = mean(ys) - m1*mean(xs)
    
    return m1, b1

m1, b1 = best_fit_slope_and_intercept(xs,ys)

#This prints the slope and intercept of my data
print(m1,b1)

#This allows the prediction of other values not necessary, but useful.
regression_line = []
for x in xs:
    regression_line.append((m1*x)+b1)

#Plot stuff
plt.style.use('fast')
plt.scatter(xs,ys, c='black')
plt.plot(xs, regression_line)
plt.title('$T^2/4\pi^2$ vs Mass No Speaker Box')
plt.xlabel('Mass (kg)')
plt.ylabel('$T^2/4\pi^2$')
plt.ylim((1.0E-05,4.0E-05))
plt.xlim((0,.035))
plt.show(1)





#Emperical data from experiment
T24pi2_vals = np.array([3.37320331E-06, 3.86465451E-06, 4.47188637E-06, 4.85069667E-06, 5.40380376E-06, 5.92823234E-06, 6.44979084E-06], dtype=np.float64)
m_vals = np.array([0, .005, .010, .015, .020, .025, .030], dtype=np.float64)

#defining variables from experimental data
xs2 = m_vals
ys2 = T24pi2_vals

#Making a line of best fit
def best_fit_slope_and_intercept(xs2,ys2):
    m2 = (((mean(xs2)*mean(ys2)) - mean(xs2*ys2)) /
         ((mean(xs2)*mean(xs2)) - mean(xs2*xs2)))
    
    b2 = mean(ys2) - m1*mean(xs2)
    
    return m2, b2

m2, b2 = best_fit_slope_and_intercept(xs2,ys2)

#This prints the slope and intercept of my data
print(m2,b2)

#This allows the prediction of other values not necessary, but useful.
regression_line = []
for x in xs2:
    regression_line.append((m2*x)+b2)

#Plot stuff
plt.style.use('fast')
plt.scatter(xs2,ys, c='black')
plt.plot(xs2, regression_line)
plt.title('$T^2/4\pi^2$ vs Mass No Speaker Box')
plt.xlabel('Mass (kg)')
plt.ylabel('$T^2/4\pi^2$')
plt.ylim((3.0E-06,7.0E-06))
plt.xlim((0,.035))
plt.show(2)



