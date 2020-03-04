# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:37:51 2018

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:28:59 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

d_vals = [1.9,1.272,0.955,1.574,1.27]
C_vals = [6.10,4.13,3.25,5.20,4.20] 

N = len(d_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + C_vals[i]
    sum_x = sum_x + d_vals[i]
    sum_xy = sum_xy + d_vals[i]*C_vals[i]
    sum_x_squared = sum_x_squared + d_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (C_vals[i] - A - B*d_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

x_plot = np.arange(.6,3)
plt.ylim(2.5,7.5)

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(d_vals,C_vals, color = 'g', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('Diameter (m)')
my_fig.set_ylabel('Circumference (m)')
my_fig.set_title('Circumference vs Diameter')
plt.savefig('Determining Pi.png', dpi=300)


