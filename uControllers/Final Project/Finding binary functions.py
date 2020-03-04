# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 02:04:16 2019

@author: maxhu
"""

import numpy as np
import matplotlib.pyplot as plt

def A(x):
    return np.cos(x)
def B(y):
    return np.cos(y)
   
x = np.linspace(-1,10,5000)
y = x*2.7
plt.plot(A(y), A(x), 'm')

def convert_to_bin(x):
    new = []
    whole = []
    R = []
    
    for i in x:
        whole.append(int(i))
        if int(i) == 0:
            R.append(i)
        else:
            R.append(i % int(i))
            
    bin_whole = []
    bin_R = []
    d = ''
    
    def reverse(num):
      return int(num[::-1])
    
    for i in whole:
        new = np.abs(i)
        d = ''
        if new == 0:
            d = 0
        else:
            d = ''
            while new > 0:
                if new % 2 == 0:
                    d = d + '0'
                elif new % 2 == 1:
                    d = d + '1'
                new = new // 2
            d = reverse(d)
        if i < 0:
            d = -d
        bin_whole.append(d)
    
    for i in R:
        R_more = np.abs(i)
        if R_more == 0:
            d = .0
        else:
            d = '.'
            while R_more != 0:
                R_more = R_more * 2
                if R_more > 1:
                    d = d + '1'
                    
                elif R_more < 1:
                    d = d + '0'
                R_more = R_more % 1
                
                if R_more == 0:
                    d = d + '1'
            d = float(d)
#        d = round(d,20)
        if i < 0:
            d = -d
        bin_R.append(d)
    
    binary_equiv = []
    
    for i in range(len(bin_whole)):
        binary_equiv.append(bin_R[i] + bin_whole[i])
    
    return binary_equiv

N = 12
v_ref = 5
G = 1
digital = max(binary_equiv)
v_out = (v_ref * digital * G) / 2**N
print(v_out)


