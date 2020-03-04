# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:16:31 2019

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:57:05 2019

@author: maxhu
"""
import numpy as np
import matplotlib.pyplot as plt

y_values = [4.114, 5.218, 5.810]
x_values = [0.0036765, .0033841, .0032584]
N = len(x_values)
sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + y_values[i]
    sum_x = sum_x + x_values[i]
    sum_xy = sum_xy + x_values[i]*y_values[i]
    sum_x_squared = sum_x_squared + x_values[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
global A
global B
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0

for i in range (0,N):
    deviation = deviation + (y_values[i] - A - B*x_values[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)


def my_fit(x):#Plot this in your figure for linear regression line
    return A + B*x
x = np.linspace(.003,.004)
lnk = [4.114, 5.218, 5.810]
T = [0.0036765, .0033841, .0032584]
fig = plt.figure(1,figsize=(15, 5))
plt.xlim((.003,.004))

my_fig = fig.add_subplot(111)
plt.scatter(x_values, y_values, label = '$-E_a/R = -4006.87$')
plt.plot(x, my_fit(x))
plt.legend(loc = 'best')
my_fig.set_xlabel('$1/T$', fontsize=15)
my_fig.set_ylabel('$ln(k)$', fontsize=15)
my_fig.set_title('Arrhenius Plot', fontsize=15)
plt.savefig('Lab1.png', dpi=300)
