#Plotting Cap discharge
#max huggins
#1/30/19

import matplotlib.pyplot as plt
import numpy as np

#define data arrays
ONEktime_data = []
ONEkvoltage_data = []

#read in data for 1k resistor discharge
lines = np.loadtxt('CapData1k.txt', delimiter=',')
for line in lines:
    ONEktime_data.append(line[0])
    ONEkvoltage_data.append(line[1])

#Exponential decay function
def my_func(x,a,b):
    return a*np.exp(-b*x)

#have to do the following to use the time data in the exp function
ONEkfit_time_data = np.array(ONEktime_data)
##################################################################
#define data arrays
TENktime_data = []
TENkvoltage_data = []

#read in data 10k resistor discharge
lines = np.loadtxt('CapData10k.txt', delimiter=',')
for line in lines:
    TENktime_data.append(line[0])
    TENkvoltage_data.append(line[1])

#have to do the following to use the time data in the exp function
TENkfit_time_data = np.array(TENktime_data)
##################################################################
#define data arrays
TWENTYktime_data = []
TWENTYkvoltage_data = []

#read in data 20k resistor discharge
lines = np.loadtxt('CapData20k.txt', delimiter=',')
for line in lines:
    TWENTYktime_data.append(line[0])
    TWENTYkvoltage_data.append(line[1])

#have to do the following to use the time data in the exp function
TWENTYkfit_time_data = np.array(TWENTYktime_data)
#################################################################
#define data arrays
THIRTYktime_data = []
THIRTYkvoltage_data = []

#read in data 30k resistor discharge
lines = np.loadtxt('CapData30k.txt', delimiter=',')
for line in lines:
    THIRTYktime_data.append(line[0])
    THIRTYkvoltage_data.append(line[1])

#have to do the following to use the time data in the exp function
THIRTYkfit_time_data = np.array(THIRTYktime_data)
#################################################################
#make plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#make an xy scatter plot
plt.scatter(ONEktime_data,ONEkvoltage_data,color='r', label = '1k Discharge', s=1, marker = 'o') #For 1k R
plt.scatter(TENktime_data,TENkvoltage_data,color='g', label = '10k Discharge', s=1, marker = '^') #For 10k R
plt.scatter(TWENTYktime_data,TWENTYkvoltage_data,color='b', label = '20k Discharge', s=1, marker = 's') #For 20k R
plt.scatter(THIRTYktime_data,THIRTYkvoltage_data,color='black', label = '30k Discharge', s=1, marker = 'x') #For 30k R
#add the exp curve w/ guesses for the constants a and b
plt.plot(ONEkfit_time_data,my_func(ONEkfit_time_data,3.2,769.2),color = 'r', label = '1k R fit', linestyle = '-')#For 1k R
plt.plot(TENkfit_time_data,my_func(TENkfit_time_data,3.2,78.4),color = 'g', label = '10k R fit', linestyle = '--')#For 10k R
plt.plot(TWENTYkfit_time_data,my_func(TWENTYkfit_time_data,3.2,38.5),color = 'b', label = '20k R fit', linestyle = ':')#For 20k R
plt.plot(THIRTYkfit_time_data,my_func(THIRTYkfit_time_data,3.2,25.79),color = 'black', label = '30k R fit', linestyle = '-.')#For 30k R

#label axes
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_title('1 uF Capacitor Discharge')
plt.legend(loc = 'best')
ax.text(0.4,1.5, 'Exponential decay!')

#save it (I saved it as a pdf to get maximum resolution)
plt.savefig('CapDischargeAll.pdf', format='pdf')
