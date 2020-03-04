# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:18:46 2019

@author: maxhu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 6\Week 2\Data\I2.xlsx', sheet_name='I2')
df = pd.DataFrame(data, columns= ['Wavelength'])
test = df.values.tolist()
w  = [val for sublist in test for val in sublist]

data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 6\Week 2\Data\I2.xlsx', sheet_name='I2')
df = pd.DataFrame(data, columns= ['Abs'])
test = df.values.tolist()
a  = [val for sublist in test for val in sublist]

A = np.array(a)
W = np.array(w)

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

plt.figure(figsize=(10,7))
#plt.plot(W, A)
plt.xlim(510,648)

def local_minima(x, y, thresh_percent, low_limit, high_limit, closeness):
    mini = min(y)
    maxi = max(y)
    global y_min
    global x_min
    y_min = []
    x_min = []
    counter = 0
    
    for q in range(0,len(y)):
         if y[q] < maxi and y[q] > mini:
             counter = counter + 1
         
    threshhold = int(thresh_percent * (counter))
    
    for i in range(1,len(y)-1):
        if y[i] < y[i+1] and y[i] < y[i-1]:
            for l in range(0,threshhold):
                if i + l > len(y)-1:
                    break
                elif y[i-l] > y[i] and y[i+l] > y[i]:
                    if l == threshhold-1:
                        y_min.append(y[i])
                        x_min.append(x[i])
                        i = i + l
                    else:
                        pass
                else:
                    pass
    for m in range(0,len(x_min)-1):
        if x_min[m] < low_limit or x_min[m] > high_limit or x_min[m] > 580 and (x_min[m+1] / x_min[m]) > closeness:
            y_min[m] = np.nan
            x_min[m] = np.nan
        else:
            pass
        
    plt.scatter(x_min,y_min, s = 15, color='m')
    return print("# of minima ", len(y_min))

smoothness = 4
local_minima(W, smooth(A,smoothness), .01, 520, 640,.996)
plt.plot(W, smooth(A,smoothness), color='black')

file = open('I2_mins.txt', 'w')
for n in range(len(y_min)):
    #Write the data as comma delimites
    file.write(str(round(x_min[n],2)) + ',' + str(round(y_min[n],5)) + '\n')
#always close the file you are using

file.close()
