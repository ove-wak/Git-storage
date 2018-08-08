# 数据输入方式1:本地txt文件存储
# 数据输出方式1:输出到本地excel文件
import os,time
from dataProcess import DataProcess
from fingerprintUpdate import FingerprintUpdate
# 定义开始更新和结束更新以及增量更新时间间隔的全局变量
# **准备放到脚本中保存
global_begin_time = 0
global_end_time = 0
global_interval_time = 0
# 位置
global_attr = 0
# ap_mac数值对，ap的mac地址和对应ap的失效次数
global_ap_mac = {}
# 模型序号，每次底图采集模型序号加1
global_model_num = 0    
# 更新序号，每次底图采集置0，后续递加1
global_update_num = 0 


class GuiContent:   
    # 处理数据
    # 参数:  
    # 说明:按照模型和图大小将每组数据处理为一个数组并保存 
    def data_process(self,address,begin_time,end_time):
        d_process = DataProcess()
        ap_m = d_process.process_data(address,begin_time,end_time)
        # 底图处理
        if end_time == global_begin_time:                   
            #保存方式：写入到数据库中
            global_model_num = global_model_num + 1
            global_update_num = 0
        # 更新数据处理 
        else：
            global_update_num = global_update_num + 1

        flag = d_process.save_data(global_attr,global_model_num,global_update_num,global_ap_mac,ap_m)
        if flag == 1:
            print(str(x)+"完成.")
        else:
            print(str(x)+"失败.")
            return -1
        # 全部操作结束断开连接
        d_process.close_connect()
        return 1

    # 指纹更新
    # 参数:model_num更新位置
    # 两种保存方式
    def fingerprint_update(self):
        d_process = DataProcess()
        f_update = FingerprintUpdate()
        # **以当前坐标建立二维坐标系
        # c_x = 
        # c_y = 
        ap_m = []
        for x in range(len(ap_mac)):
            ditu = d_process.get_data(global_model_num,0,ap_mac[x],c_x,c_y)
            f_update.get_none(ditu,x)
            for y in range(1,(model_num+1)):
                data = d_process.get_data(y,0,ap_mac[x],c_x,c_y)
                f_update.get_median(ditu,data,y,x)
            ap_m.append(f_update.training(model_num,ditu,x))
        # ****逻辑需要修改，应将每次网络模型参数保存，下一次直接使用，而不是每次都全部执行一遍

        # 增量更新结果保存到数据库中
        flag = d_process.save_data(global_attr,model_num,update_num,ap_mac,ap_m)
        if flag == 1:
            print(str(model_num)+"完成.")
        else:
            print(str(model_num)+"失败.")
            return -1

        # 全部操作结束断开连接
        d_process.close_connect()
        f_update.mlab_stop(ap_mac)
        return 1
    
    def forever_update(self):
        # 无限循环*待补充
            #获取当前时间进行比较
            if "time" == global_begin_time:
                #在开始时间生成一次底图
                self.data_process(global_attr,"#*前一天的结束时间",global_begin_time)
            else if "#*每个时间段进行指纹更新":
                # 指纹库更新
                self.data_process(global_attr,"#*开始时间","#*结束时间")
                g.fingerprint_update()



#操作流程:
#1.保存元数据
#2.数据处理
#3.指纹更新