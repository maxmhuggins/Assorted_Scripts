# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:28:13 2019

@author: maxhu
"""
#============================================================================#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#============================================================================#
data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 6\Week 2\Data\Br2.xlsx', sheet_name='Br2')
df = pd.DataFrame(data, columns= ['Wavelength'])
test = df.values.tolist()
w  = [val for sublist in test for val in sublist]

data = pd.read_excel (r'C:\Users\maxhu\Documents\PChem\Lab 6\Week 2\Data\Br2.xlsx', sheet_name='Br2')
df = pd.DataFrame(data, columns= ['Abs'])
test = df.values.tolist()
a  = [val for sublist in test for val in sublist]
#============================================================================#
A = np.array(a)
W = np.array(w)
#============================================================================#
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def local_minima(x, y, thresh_percent, low_limit, high_limit):
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
    for m in range(0,len(x_min)):
        if x_min[m] < low_limit or x_min[m] > high_limit:
            y_min[m] = np.nan
            x_min[m] = np.nan
    plt.scatter(x_min,y_min, s = 15, color='m', label='Local Minima')
    return print("# of minima ", len(y_min))
#============================================================================#
size = 10
fig = plt.figure(1,figsize=(10,13))
fig.suptitle('Molecular Spectra for $Br_2$', fontsize=15)
my_fig = fig.add_subplot(211)
plt.plot(W, A, color='black', label='Raw $Br_2$ Spectral Data')
plt.ylabel('Absorbance', fontsize=size)
plt.xlabel('Wavelength (nm)', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.xlim(510,605)
my_fig = fig.add_subplot(212)
plt.plot(W, smooth(A,2), color='black', label='$Br_2$ Spectral Data Smoothed')
local_minima(W, smooth(A,2), .005, 520, 650)
plt.ylabel('Absorbance', fontsize=size)
plt.xlabel('Wavelength (nm)', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.xlim(510,605)
plt.savefig('Br_2.png', dpi=900)
plt.legend(loc='best')
#============================================================================#
file = open('Br2_mins.txt', 'w')
for n in range(len(y_min)):
    #Write the data as comma delimites
    file.write(str(round(x_min[n],2)) + ',' + str(round(y_min[n],5)) + '\n')
#always close the file you are using

file.close()
#============================================================================#
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
        
    plt.scatter(x_min,y_min, s = 15, color='m', label='Local Minima')
    return print("# of minima ", len(y_min))

size = 10
smoothness = 4
fig = plt.figure(2,figsize=(10,13))
fig.suptitle('Molecular Spectra for $I_2$', fontsize=15)
my_fig = fig.add_subplot(211)
plt.plot(W, A, color='black', label='Raw $I_2$ Spectral Data')
plt.ylabel('Absorbance', fontsize=size)
plt.xlabel('Wavelength (nm)', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.xlim(510,648)
my_fig = fig.add_subplot(212)
plt.plot(W, smooth(A,smoothness), color='black', label='$I_2$ Spectral Data Smoothed')
local_minima(W, smooth(A,smoothness), .01, 520, 640,.996)
plt.ylabel('Absorbance', fontsize=size)
plt.xlabel('Wavelength (nm)', fontsize=size)
plt.legend(loc='best', fontsize=size)
plt.xlim(510,648)
plt.savefig('I_2.png', dpi=900)
plt.legend(loc='best')

file = open('I2_mins.txt', 'w')
for n in range(len(y_min)):
    #Write the data as comma delimites
    file.write(str(round(x_min[n],2)) + ',' + str(round(y_min[n],5)) + '\n')
#always close the file you are using

file.close()
