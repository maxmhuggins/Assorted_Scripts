# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:28:59 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np
L = .349

x_vals = [3,5,7,9,11,13,15,17,19,21]
y_vals = [791,1287,1683,2162,2653,3128,3597,4087,4554,5034]

N = len(x_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + y_vals[i]
    sum_x = sum_x + x_vals[i]
    sum_xy = sum_xy + x_vals[i]*y_vals[i]
    sum_x_squared = sum_x_squared + x_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (y_vals[i] - A - B*x_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

x_plot = np.arange(0,30)
plt.ylim(0,6000)

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

plt.scatter(x_vals,y_vals, color = 'b', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '--')
plt.ylabel('Resonant Frequency (Hz)')
plt.xlabel('Harmonic')
plt.title('Harmonic vs Resonant Frequency')
plt.savefig('lab 6 plot.png', dpi=300)

#Speed of Sound
SOS = B*L*4
print('The determined speed of sound is:')
print (SOS)

#####################################
#Calculating Error in slope (A) for Speed of sound
efreqabs = 10
sumyerr = np.sqrt(10*efreqabs**2)
sumxyerr = sumyerr*10
AbsErrB = np.sqrt((sum_x*sumyerr)**2+(19*sumxyerr)**2)/Delta
#Calculating Error in Speed of Sound
errmeter = .001
ErrSOS = SOS*4*np.sqrt((errmeter/L)**2+(AbsErrB/B)**2)
print ('The error in the speed of sound is:')
print(ErrSOS)
