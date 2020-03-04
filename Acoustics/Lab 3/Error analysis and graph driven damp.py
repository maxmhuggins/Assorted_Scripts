# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:53:38 2018

@author: maxhu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:48:10 2018

@author: maxhu
"""


import matplotlib.pyplot as plt
import numpy as np

t_vals = [6.4, 19.2, 32, 44.8, 56.8, 68.8, 80.8, 93.6, 105, 118, 131, 142, 154, 168]
ln_v_vals = [6.342121419, 5.840641657, 5.66296048, 5.214935758, 5.023880521, 4.477336814, 4.477336814, 3.871201011, 3.871201011, 3.465735903, 3.688879454, 3.465735903, 3.17805383, 2.772588722]

N = len(t_vals)

sum_y = 0
sum_x = 0
sum_xy = 0
sum_x_squared = 0

for i in range(0,N):
    sum_y = sum_y + ln_v_vals[i]
    sum_x = sum_x + t_vals[i]
    sum_xy = sum_xy + t_vals[i]*ln_v_vals[i]
    sum_x_squared = sum_x_squared + t_vals[i]**2
    
Delta = N*sum_x_squared - (sum_x)**2
A = (sum_x_squared*sum_y - sum_x*sum_xy) / Delta
B = (N*sum_xy - sum_x*sum_y) / Delta

deviation = 0
for i in range (0,N):
    deviation = deviation + (ln_v_vals[i] - A - B*t_vals[i])**2
    
sigma_y = np.sqrt(deviation / (N-2))

sigma_A = sigma_y*np.sqrt(sum_x_squared/Delta)
sigma_B = sigma_y*np.sqrt(N/Delta)

print('The best estimate for A is: ', A)
print("The best estimate for the uncertainty in A is: ", sigma_A)

print('The best estimate for B is: ', B)
print("The best estimate for the uncertainty in B is: ", sigma_B)

x_plot = np.arange(0,180)
plt.ylim((2,7))

def my_fit(x):
    return A + B*x

fig = plt.figure(1)

my_fig = fig.add_subplot(1,1,1)
my_fig.grid(True)
plt.scatter(t_vals,ln_v_vals, color = 'g', marker='o')
plt.plot(x_plot,my_fit(x_plot), color ='black', linestyle = '-')
my_fig.set_xlabel('Time (s)')
my_fig.set_ylabel('ln|V|')
my_fig.set_title('ln|V| vs Time Elapsed')
plt.savefig('damped driven.png', dpi=300)
