# -*- coding: UTF-8 -*-
# 核心指纹更新模块
# 通过excel文件中数据生成中间数据并通过oselm进行训练,最终得到完整指纹库
import os,time,numpy,shutil
from pymatbridge import Matlab

class FingerprintUpdate:
    def __init__(self):             
        self.mlab = Matlab()
        self.mlab.start()
        # 该文件无用,只是为了避免一个路径引起的bug
        res = self.mlab.run_func('C:/Users/ovewa/Desktop/git-storage/OS-ELM-matlab/test.m',1)

    # 生成中间数据
    def get_median(self,ditu,data,model_num,ap_num):
        if os.path.isdir('middata'+str(ap_num)+'/'):
            pass
        else:
            os.mkdir('middata'+str(ap_num)+'/')
        with open('middata'+str(ap_num)+'/'+str(model_num)+'.txt','wt') as f:
            for x in range(len(data)):
                for y in range(len(data[0])):
                    if int(data[x][y]) != 0 and int(ditu[x][y]) != 0:
                        f.write(str(data[x][y]/ditu[x][y] - 1)+" "+str(x)+" "+str(y)+"\n")

    def get_none(self,ditu,ap_num):
        if os.path.isdir('middata'+str(ap_num)+'/'):
            pass
        else:
            os.mkdir('middata'+str(ap_num)+'/')
        with open('middata'+str(ap_num)+'/none.txt','wt') as f:
            for x in range(len(ditu)):
                for y in range(len(ditu[0])):
                    f.write(str(0)+" "+str(x)+" "+str(y)+"\n")

    # 训练过程
    # 可优化
    # 1是训练条件不同结果不同
    # 2是随机参数不同结果不同
    # 多次训练取最优解
    def training(self,model_num,ditu,ap_num): 
        # 初始训练
        res = self.mlab.run_func('OSELM_initial_training.m','middata'+str(ap_num)+'/1.txt',10,'sin',nargout=5)
        IW = res['result'][0]
        Bias = res['result'][1]
        M = res['result'][2]
        beta =res['result'][3]
        # 增量学习
        # ####!!!添加将每一次增量学习结果的误差输出出来并可视化
        for x in range(2,(model_num+1)):
            res = self.mlab.run_func('OSELM_increase_study.m','middata'+str(ap_num)+'/'+str(x)+'.txt',IW,Bias,M,beta,'sin',1,nargout=4)
            IW = res['result'][0]
            Bias = res['result'][1]
            M = res['result'][2]
            beta =res['result'][3]
        # 获取完整指纹库
        res = self.mlab.run_func('OSELM_test_value.m','middata'+str(ap_num)+'/none.txt',IW,Bias,beta,'sin')
        result = res['result']
        y = 0
        data = []
        for i in range(len(ditu)):
            data.append([])
            for j in range(len(ditu[0])):
                data[i].append(-1)

        for x in range(len(result)): 
            ###重点,现在直接将初次训练结果保存,没有进行比较分析,待完善
            data[x%10][y] = int(ditu[x%10][y]*(result[x]+1))
            if (x+1)%10 == 0:
                y=y+1
        return data

    def mlab_stop(self,ap_mac):
        self.mlab.stop()
        # 删除中间文件
        for x in range(len(ap_mac)):
            if os.path.isdir('middata'+str(x)+'/'):
                shutil.rmtree('middata'+str(x)+'/')
