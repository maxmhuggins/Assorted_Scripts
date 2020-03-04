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

#plt.figure()
#hmap = plt.imshow(map_list[0], vmin=20, vmax=120)
#plt.colorbar(hmap)

fig = plt.figure(figsize =(15,20))
fig.suptitle('Heatmap of Hotplate', fontsize=24)

ax = fig.add_subplot(3,2,1)
#my_fig = fig.add_subplot(231,aspect='equal')
hmap = plt.imshow(map_list[0], cmap = 'hot', vmin=20, vmax=120)
ax.set_xlabel('x-position')
ax.set_ylabel('y-position')
plt.colorbar(hmap)

ax = fig.add_subplot(3,2,2)
#my_fig = fig.add_subplot(231,aspect='equal')
hmap = plt.imshow(map_list[25], cmap = 'hot', vmin=20, vmax=120)
ax.set_xlabel('x-position')
ax.set_ylabel('y-position')
plt.colorbar(hmap)

ax = fig.add_subplot(3,2,3)
#my_fig = fig.add_subplot(231,aspect='equal')
hmap = plt.imshow(map_list[60], cmap = 'hot', vmin=20, vmax=120)
ax.set_xlabel('x-position')
ax.set_ylabel('y-position')
plt.colorbar(hmap)

ax = fig.add_subplot(3,2,4)
#my_fig = fig.add_subplot(231,aspect='equal')
hmap = plt.imshow(map_list[120], cmap = 'hot', vmin=20, vmax=120)
ax.set_xlabel('x-position')
ax.set_ylabel('y-position')
plt.colorbar(hmap)

ax = fig.add_subplot(3,2,5)
#my_fig = fig.add_subplot(231,aspect='equal')
hmap = plt.imshow(map_list[175], cmap = 'hot', vmin=20, vmax=120)
ax.set_xlabel('x-position')
ax.set_ylabel('y-position')
plt.colorbar(hmap)

ax = fig.add_subplot(3,2,6)
#my_fig = fig.add_subplot(231,aspect='equal')
hmap = plt.imshow(map_list[240], cmap = 'hot', vmin=20, vmax=120)
ax.set_xlabel('x-position')
ax.set_ylabel('y-position')

plt.colorbar(hmap)
plt.savefig('six_plots.pdf', format = 'pdf')
plt.close()

#file_name = './Heatmaps/{:03d}_hotplate_heatmap.jpg'
#
#for i in range(len(map_list)):
#    
#    fig = plt.figure()
#    my_fig = fig.add_subplot(111,aspect='equal')
#    hmap = plt.imshow(map_list[i], vmin=20, vmax=120)
#    plt.colorbar(hmap)
#    my_fig.set_xlabel('x-position')
#    my_fig.set_ylabel('y-position')
#    my_fig.set_title('Heatmap of Hotplate')
#    plt.savefig(file_name. format(i))
#    plt.close()
