# -*- coding: UTF-8 -*-
# 通过excel文件中数据生成中间数据并通过oselm进行训练,最终得到完整指纹库
import xlrd,os,time,numpy
from pymatbridge import Matlab
from dataToExcel import DataToExcel

sheet = 0 # 单ap训练,定义ap序号

class DataPreprocess:
    def __init__(self):
        file = xlrd.open_workbook('excel/底图.xls')
        table = file.sheets()[sheet]  #通过索引顺序获取工作表
        nrows = table.nrows #行数              
        self.mlab = Matlab()
        self.mlab.start()
        # 该文件无用,只是为了避免一个路径引起的bug
        res = self.mlab.run_func('C:/Users/ovewa/Desktop/git-storage/OS-ELM-matlab/test.m',1)
        self.ditu = []
        for i in range(1,nrows):
            self.ditu.append(table.row_values(i)[1:])

    # 生成中间数据
    def get_median(self):
        for j in range(1,20):
            file = xlrd.open_workbook('excel/'+str(j)+'.xls')
            table = file.sheets()[sheet]  #通过索引顺序获取工作表
            nrows = table.nrows #行数
            data = []
            for i in range(1,nrows):
                data.append(table.row_values(i)[1:])
            if os.path.isdir('middata'+str(sheet)+'/'):
                pass
            else:
                os.mkdir('middata'+str(sheet)+'/')
            with open('middata'+str(sheet)+'/'+str(j)+'.txt','wt') as f:
                for y in range(len(data)):
                    for x in range(len(data[0])):
                        if int(data[y][x]) != 0 and int(self.ditu[y][x]) !=0:
                            f.write(str(data[y][x]/self.ditu[y][x] - 1)+" "+str(x)+" "+str(y)+"\n")

    def get_none(self):
        with open('middata'+str(sheet)+'/none.txt','wt') as f:
            for y in range(13):
                for x in range(10):
                    f.write(str(0)+" "+str(x)+" "+str(y)+"\n")

    # 训练过程
    # 可优化
    # 1是训练条件不同结果不同
    # 2是随机参数不同结果不同
    # 多次训练取最优解
    def training(self): 
        # 初始训练
        res = self.mlab.run_func('OSELM_initial_training.m','middata'+str(sheet)+'/1.txt',10,'sin',nargout=5)
        IW = res['result'][0]
        Bias = res['result'][1]
        M = res['result'][2]
        beta =res['result'][3]
        # 增量学习
        for x in range(2,11):
            res = self.mlab.run_func('OSELM_increase_study.m','middata'+str(sheet)+'/'+str(x)+'.txt',IW,Bias,M,beta,'sin',1,nargout=4)
            IW = res['result'][0]
            Bias = res['result'][1]
            M = res['result'][2]
            beta =res['result'][3]
        # 获取完整指纹库
        res = self.mlab.run_func('OSELM_test_value.m','middata'+str(sheet)+'/none.txt',IW,Bias,beta,'sin')
        result = res['result']

        y = 0
        data = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0]]

        for x in range(len(result)): 
            ###重点,现在直接将初次训练结果保存,没有进行比较分析,待完善
            data[x%10][y] = int(self.ditu[y][x%10]*(result[x]+1))
            if (x+1)%10 == 0:
                y=y+1
        return data

    def mlab_stop(self):
        self.mlab.stop()

# 测试环境下运行
if __name__ == "__main__":
    d = DataPreprocess()
    data = []
    for x in range(4):
        sheet = x
        #d.get_median()
        #d.get_none()
        data.append(d.training())

    excel = DataToExcel()
    excel.odte("前十组增量学习结果",data)
    d.mlab_stop()