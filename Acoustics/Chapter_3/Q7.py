# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 06:12:31 2018

@author: maxhu
"""

import matplotlib.pyplot as plt
import numpy as np

p_o = 1.2

def T(C):
    return np.cos(1/np.arctan2(C,1))

C_start = 1
C_end = 10
num = 2000

CKR = np.linspace(C_start,C_end,num)

fig = plt.figure(1)
my_fig = fig.add_subplot(1,1,1)
plt.plot(CKR, T(CKR), color='darkblue', label='c=.2', linestyle = '-')

my_fig.set_xlabel('kr')
my_fig.set_ylabel('Phase of the specific acoustic impedence')
my_fig.set_title('Phase of the Specific Acoustic Impedence vs kr')
plt.savefig('Q7', dpi=300)
