#Plotting HotPlate Stuff
#max huggins
#2/20/19

import matplotlib.pyplot as plt
import numpy as np
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
#Making XY grid points
x_values = np.linspace(-6, 6, 5)
y_values = np.linspace(-6, 6, 5)

#Making a grid
X,Y = np.meshgrid(x_values,y_values)
#Plotting
file_name = 'hotplate_contour.png'
w, h = plt.figaspect(1.)
fig = plt.figure(figsize=(w, h))
my_fig = fig.add_subplot(111,aspect='equal')
my_fig.set_xlabel('x-pos')
my_fig.set_ylabel('y-pos')
my_fig.set_title('Temperature Sensing on Hotplate')

for t in range(len(TempDataLists)):
    Z = TempDataLists[t]
    n_lines = 100
    plt.contourf(X,Y,Z, n_lines, cmap=plt.cm.jet)
plt.tight_layout()
plt.savefig(file_name, dpi=300)
plt.show()
plt.close()
