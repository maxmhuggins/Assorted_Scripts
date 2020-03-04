#Plotting HotPlate Stuff
#max huggins
#2/20/19

import matplotlib.pyplot as plt
import numpy as np

#define data arrays
time_data = []
temp_data = []

file_name = '{:03d}HotData{:01d}'

#read in data
lines = np.loadtxt('HOTPLATETESTING.txt', delimiter=',')
for line in lines:
    file = open('./Data/', 'w')
