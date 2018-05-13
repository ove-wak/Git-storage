import numpy as np
from matplotlib.pyplot import plot, show

line_datas = []
waves = []
with open('d://地震局0425/dawu/g15118.dmp','r') as file_read:
    line_datas = file_read.readlines() # 读取全部行数据
for x in range(len(line_datas)):
    if x >= 3:
        line_datas[x] = line_datas[x].split()
        for t in line_datas[x]:
            waves.append(float(t))
print(waves[0])
transformed = np.fft.fft(waves)  #使用fft函数对信号进行傅里叶变换。
transformed = transformed[0:int(len(transformed)/2)] # 因为变换后是对称的,因此删除一半
print(len(transformed))
print(transformed[1])  
plot(transformed)  #使用Matplotlib绘制变换后的信号。
show()