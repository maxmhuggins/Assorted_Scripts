#Plotting Test data
#max huggins
#2/17/19

import matplotlib.pyplot as plt
import numpy as np

R_1 = 98.5
R_2 = 98.4

#define data arrays
time_data = []
voltage_data = []

#read in data
lines = np.loadtxt('Test1NEWCode.txt', delimiter=',')
for line in lines:
    time_data.append(line[0] / 3600)
    v_in = ((R_1 + R_2) / (R_1)) * line[1]
    voltage_data.append(v_in)

#make plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(time_data,voltage_data,color='b', s = 1)

#label axes
ax.set_xlabel('Time (hr)')
ax.set_ylabel('Battery Voltage (V)')
ax.set_title('9V Energizer Battery Voltage Discharge \n Through $200 \Omega$')
plt.legend(loc = 'best')

#save it
plt.savefig('TestDataNEW_1.png')

