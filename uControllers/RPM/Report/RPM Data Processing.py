# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:49:07 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

RPMs = [[] for i in range(0,21)]
duty_cycles = [[] for i in range(0,21)]

for i in range(0,21):
    lines = np.loadtxt('../RPMDATA/RPMs{}.txt'.format(i), delimiter=',')
    for line in lines:
        RPMs[i].append(line[1])
        duty_cycles[i].append(line[0])
        
plt.figure(figsize=(20,10))
for i in range(7,18):
    plt.plot(duty_cycles[i],RPMs[i], '.-', label = 'Time after % change: {}s'.format(i))
plt.legend(loc='best')
plt.xlabel('Duty Cycle as %', fontsize=(12))
plt.ylabel('Revolutions per Minute (rpm)', fontsize=(12))
plt.title('RPM vs Duty Cycle at Various Wait Times', fontsize=(12))
plt.savefig('RPM_Data')

plt.figure(figsize=(20,10))
plt.plot(duty_cycles[17],RPMs[17], '.-', color = 'black', label = 'Time after % change: 17s')
plt.legend(loc='best')
plt.xlabel('Duty Cycle as %', fontsize=(12))
plt.ylabel('Revolutions per Minute (rpm)', fontsize=(12))
plt.title('RPM vs Duty Cycle at Various Wait Times', fontsize=(12))
plt.savefig('RPM_Data_Single')

