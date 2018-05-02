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
# x = np.linspace(0, 2 * np.pi, 30) #创建一个包含30个点的余弦波信号
# print(x)
# wave = np.cos(x)
# print(wave)
transformed = np.fft.fft(waves)  #使用fft函数对余弦波信号进行傅里叶变换。
print(transformed[1])  #对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
plot(transformed)  #使用Matplotlib绘制变换后的信号。
show()