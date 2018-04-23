import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

def func(x, a, b, c):  
    return a * np.exp(-b * x) + c  

with open("10_1_cdf.csv","r") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for i in read:
          data = i
for x in range(len(data)):
    data[x]= float(data[x])
data = np.sort(data)
d_x = []
d_y = []
for x in range(0,31):
    temp = 0
    for d in data:
        if d <= x:
            temp = temp+1
    d_y.append(temp/len(data))
    d_x.append(x)
# 拟合
# popt, pcov = curve_fit(func, d_x, d_y)  
# #popt数组中，三个值分别是待求参数a,b,c  
# d_y = [func(i, popt[0],popt[1],popt[2]) for i in d_x]  
plt.plot(d_x,d_y,label="9 AM",linestyle='--')

with open("10_2_cdf.csv","r") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for i in read:
          data = i
for x in range(len(data)):
    data[x]= float(data[x])
data = np.sort(data)
d_x = []
d_y = []
for x in range(0,31):
    temp = 0
    for d in data:
        if d <= x:
            temp = temp+1
    d_y.append(temp/len(data))
    d_x.append(x)
# 拟合
# popt, pcov = curve_fit(func, d_x, d_y)  
# #popt数组中，三个值分别是待求参数a,b,c  
# d_y = [func(i, popt[0],popt[1],popt[2]) for i in d_x]  
plt.plot(d_x,d_y,label="2 PM",linestyle='-.')

with open("10_3_cdf.csv","r") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for i in read:
          data = i
for x in range(len(data)):
    data[x]= float(data[x])
data = np.sort(data)
d_x = []
d_y = []
for x in range(0,31):
    temp = 0
    for d in data:
        if d <= x:
            temp = temp+1
    d_y.append(temp/len(data))
    d_x.append(x)
# 拟合
# popt, pcov = curve_fit(func, d_x, d_y)  
# #popt数组中，三个值分别是待求参数a,b,c  
# d_y = [func(i, popt[0],popt[1],popt[2]) for i in d_x]  
plt.plot(d_x,d_y,label="7 PM")

plt.xlabel("RSS prediction error[dB]",fontsize=20)
plt.ylabel("CDF",fontsize=20)
plt.axis([0,30,0,1])
plt.grid(linestyle='--')
plt.legend(loc=4,fontsize=20)
plt.show()