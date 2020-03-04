# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:49:20 2019

@author: maxhu
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#=================================================================#
values = []
num = np.arange(0,1000)
#x_vals = np.linspace(73,73,100)
lines = np.loadtxt('SonicRanger.txt')
values.append(lines)
#=================================================================#
fig = plt.figure(figsize = (20,10))
plt.scatter(values, num)
#plt.plot(x_vals,num, 'm')
plt.show()
np.histogram(values)
#=================================================================#
num_bins = 30
# the histogram of the data
fig = plt.figure(figsize = (20,10))
n, bins, patches = plt.hist(values, num_bins, normed = 1)
# add a 'best fit' line
y = mlab.normpdf(bins, np.mean(values), np.std(values))
plt.plot(bins, y, 'r--')
plt.xlabel('Distance')
plt.ylabel('Occurence')
plt.title(r'Histogram of Sonic Ranger Data')
# Tweak spacing to prevent clipping of ylabel
plt.show()
#=================================================================#

#def reject_outliers(data, m):
#    d = np.abs(data - np.median(data))
#    mdev = np.median(d)
#    s = d/mdev if mdev else 0.
#    return data[s<m]

#new_values = np.array([reject_outliers(values, 2)])

    
#fig = plt.figure(figsize = (20,10))
#plt.scatter(values, num)
#plt.plot(x_vals,num, 'm')
#plt.show()
#np.histogram(values)
#=================================================================#
#num_bins = 30
## the histogram of the data
#fig = plt.figure(figsize = (20,10))
#n, bins, patches = plt.hist(new_values, num_bins, normed = 1)
## add a 'best fit' line
#y = mlab.normpdf(bins, np.mean(new_values), np.std(new_values))
#plt.plot(bins, y, 'r--')
#plt.xlabel('Distance')
#plt.ylabel('Occurence')
#plt.title(r'Histogram of Sonic Ranger Data')
## Tweak spacing to prevent clipping of ylabel
#plt.show()
