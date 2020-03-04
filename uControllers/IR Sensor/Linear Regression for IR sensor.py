# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:51:42 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

velocity_data = []
time_data = []

lines = np.loadtxt('g_Constant.txt', delimiter=',')
for line in lines:
    time_data.append(line[0])
    velocity_data.append(line[1])
    
    
N = len(time_data)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + velocity_data[i]
    sum_x = sum_x + time_data[i]
    sum_xy = sum_xy + time_data[i]*velocity_data[i]
    sum_x_squared = sum_x_squared + time_data[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0

for i in range (0,N):
    deviation = deviation + (velocity_data[i] - A - B*time_data[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)
fig = plt.figure()

def my_fit(x):#Plot this in your figure for linear regression line
    return A + B*x
x = np.linspace(1.85,2.1)
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(time_data,velocity_data,color='r')
plt.plot(x, my_fit(x))
ax.set_xlabel('Time (s)')
ax.set_ylabel('Velocity')
ax.set_title('Velocity vs Time')
plt.legend(loc = 'best')


#save it
plt.savefig('GravitationalConstantNEW.png')

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

