#Plotting thermister stuff
#max huggins
#1/30/19

import matplotlib.pyplot as plt
import numpy as np

#define data arrays
time_data = []
velocity_data = []

#read in data
lines = np.loadtxt('g_Constant.txt', delimiter=',')
for line in lines:
    time_data.append(line[0])
    velocity_data.append(line[1])

#make plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(time_data,velocity_data,color='r', label = 'data', s =1)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Velocity')
ax.set_title('Velocity vs Time')
plt.legend(loc = 'best')


#save it
plt.savefig('GravitationalConstant.png')
