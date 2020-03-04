# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:03:09 2019

@author: maxhu
"""

#Plotting HotPlate Stuff
#max huggins
#2/20/19
import numpy as np
import matplotlib.pyplot as plt
#=============================================================================#
#define data arrays
TempDataLists = [[] for i in range(0,25)]
TimeDataLists = [[] for i in range(0,25)]
#=============================================================================#
#read in data and assign to data arrays.
for i in range(1,26):
    with open('./NewDocs/TempData{}.txt'.format(i), 'r') as f:
        lines = []
        lines = f.readlines()
        temps = []
        times = []
        for n in range(len(lines)):
            stuff = lines[n].split(',')
            #only every 100th data point is used
            if n % 100 == 0:
                times.append(float(stuff[0].strip()))
                temps.append(float(stuff[1].strip()))
        for s in range(0,len(times)):
            TempDataLists[i-1].append(temps[s])
            TimeDataLists[i-1].append(times[s])
#=======================================================================#
           
#This handles plotting, labeling, and saving.
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1,1,1)

for i in range(0,25):
        plt.plot(TimeDataLists[i], TempDataLists[i], label = i+1)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (C)')
ax.set_title('Temperature of Hotplate Sensors vs. Time', fontsize=24)
plt.legend(loc = 'best')

#saving as a pdf for maximum resolution
plt.savefig('hotplateMultiple.pdf', format='pdf')
#=============================================================================#


