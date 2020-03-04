# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:57:03 2019

@author: maxhu
"""

#read in data
with open('HOTPLATETESTING.txt', 'r') as f:
    lines = []
    lines = f.readlines()

##Divide lines into 25 different data sets
N = len(lines) / 25
N = int(N)

#Make 25 different data files for the 25 different data sets
for n in range(1,26):
    with open('./NewDocs/TempData{}.txt'.format(n), 'w') as f:
        for i in range(N):
            f.write(lines[i+(n-1)*N])
            