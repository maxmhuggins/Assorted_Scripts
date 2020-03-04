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
            if n % 500 == 0:
                times.append(float(stuff[0].strip()))
                temps.append(float(stuff[1].strip()))
        for s in range(0,len(times)):
            TempDataLists[i-1].append(temps[s])
            TimeDataLists[i-1].append(times[s])
#=============================================================================#
map_list = []

for t in range(len(TimeDataLists[0])):
    temp_points = np.zeros([5,5])
    for q in range(0,5):
        y = q
        for w in range(0,5):
            x = w
            temp_points[x][y] =  TempDataLists[x + 5*y][t]
    map_list.append(temp_points)

plt.figure(1)
hmap = plt.imshow(map_list[0], vmin=20, vmax=120)
plt.colorbar(hmap)
plt.figure(2)
hmap = plt.imshow(map_list[10], vmin=20, vmax=120)
plt.colorbar(hmap)
    
        
        
        
        
        
        
#with open('./NewDocs/TempData{}.txt'.format(n), 'w') as f:
#for i in range(N):
#    f.write(lines[i+(n-1)*N])
#

    

            
#=============================================================================#
           
##This handles plotting, labeling, and saving.
#fig = plt.figure(figsize=(20,10))
#ax = fig.add_subplot(1,1,1)
#
#for i in range(0,25):
#        plt.plot(TimeDataLists[i], TempDataLists[i], label = i+1)
#
#ax.set_xlabel('Time (s)')
#ax.set_ylabel('Temperature (C)')
#ax.set_title('Temperature of Hotplate Sensors vs. Time')
#plt.legend(loc = 'best')
#
##saving as a pdf for maximum resolution
#plt.savefig('hotplateMultiple.pdf', format='pdf')
##=============================================================================#
#fig = plt.figure(figsize=(20,10))
#ax = fig.add_subplot(1,1,1)
#
#X = np.linspace(-3,3,5)
#Y = np.linspace(-3,3,5)
#
#POS = [[X],[Y]]



