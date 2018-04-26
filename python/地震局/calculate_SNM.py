#1 数据读取:单日观测文件/表
#2 数据筛选

import os,time

# 数据筛选
# 功能:去除数据缺失超过1h的无效数据，缺失数据的重力和气压值为999999.000
# 输入:数据文件所在目录
# 输出:符合条件的文件列表
def data_screening(dir_path):
    files = []
    qualified_data = []
    tt = os.walk(dir_path)
    for i in tt:
        for j in i[2]:
            if ".tsf" in j:
                files.append(j)
    for file in files:  
        flag = 0
        with open(dir_path + file, 'r') as file_read:
            while True:
                line_data = file_read.readline() # 读取整行数据
                if not line_data:
                    break
                t_d = line_data.split()
                if len(t_d) == 8:
                    if t_d[6] == '999999.000':
                        flag = flag + 1
        if flag <= 3600:
            qualified_data.append(file)
    return qualified_data

# 数据预处理
# 功能:
# 输入:
# 输出:
def data_preprocessing():
    pass

# 数据预处理
# 功能:计算每日均方差最小n的功率谱平均值
# 输入:天数值n
# 输出:
def calculate_power_spectrum(n):
    pass

dir_path = "d://地震局0425/大武原始数据/" 
data_screening(dir_path)