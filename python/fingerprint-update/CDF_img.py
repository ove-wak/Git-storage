import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

def func(x, a, b, c):  
    return a * np.exp(-b * x) + c  

with open("3_cdf.csv","r") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for i in read:
          data = i
for x in range(len(data)):
    data[x]= int(data[x])
sorted_data = np.sort(data)
yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
popt, pcov = curve_fit(func, sorted_data, yvals)  
#popt数组中，三个值分别是待求参数a,b,c  
y_t = [func(i, popt[0],popt[1],popt[2]) for i in sorted_data]  
plt.plot(sorted_data,y_t,label="After 3 days",linestyle='--')

with open("6_cdf.csv","r") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for i in read:
          data = i
for x in range(len(data)):
    data[x]= int(data[x])
sorted_data = np.sort(data)
yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1) 
print(sorted_data)
print(yvals)
popt, pcov = curve_fit(func, sorted_data, yvals)  
#popt数组中，三个值分别是待求参数a,b,c  
y_t = [func(i, popt[0],popt[1],popt[2]) for i in sorted_data]  
plt.plot(sorted_data,y_t,label="After 6 days",linestyle='-.')

with open("10_cdf.csv","r") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for i in read:
          data = i
for x in range(len(data)):
    data[x]= int(data[x])
sorted_data = np.sort(data)
yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)
popt, pcov = curve_fit(func, sorted_data, yvals)  
#popt数组中，三个值分别是待求参数a,b,c  
y_t = [func(i, popt[0],popt[1],popt[2]) for i in sorted_data]  
plt.plot(sorted_data,y_t,label="After 10 days")
plt.xlabel("RSS prediction error[dB]",fontsize=20)
plt.ylabel("CDF",fontsize=20)
plt.axis([0,30,0,1])
plt.grid(linestyle='--')
plt.legend(loc=4,fontsize=20)
plt.show()