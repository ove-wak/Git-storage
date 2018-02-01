# 数据输入方式1:本地txt文件存储
# 数据输出方式1:输出到本地excel文件
import os,time
from saveData import SaveData
from dataProcess import DataProcess
from dataToExcel import DataToExcel
from fingerprintUpdate import FingerprintUpdate

class GuiContent:   
    #数据保存 
    def save_data_event(self):   
        self.path = ""    
        self.path = input("请输入数据所在路径:")
        # 路径为空直接返回
        if self.path == "": 
            print("请输入路径!") 
            return -1
        self.path = self.path + "/"

        # 初始化
        save_data = SaveData()
        print("开始存储.")
        # 获取指定文件夹列表
        dir_names = [name for name in os.listdir(self.path) if 'WIFI+' in name]

        for dir_name in dir_names:
            phone_model = (dir_name.split('+'))[1] # 获取手机型号
            dir_path = self.path + dir_name + "/"
            # 显示进度
            print("目录 " + dir_path + " 下的文件正在存储.") 
            # 获取指定目录下所有数据的文件名
            self.file_name = []
            tt = os.walk(dir_path)
            for i in tt:
                for j in i[2]:
                    if ".txt" in j:
                        self.file_name.append(j)
            # 遍历文件夹,存储所有数据
            file_len = len(self.file_name)
            for x in range(file_len):
                file = self.file_name[x]

                begin_time = time.time()
                print(file + " saving...["+str(x+1)+"/"+str(file_len)+"]")

                # 存储单文件数据
                flag = save_data.data_save(dir_path,file,phone_model)

                if flag != 1:# 存储出错
                    print("数据库插入数据出错.")
                    print("出错位置:" + file+" "+flag)
                    save_data.close_connect()
                    return -1

                end_time = time.time()      
                print(file + " saved,time:"+str(int(end_time-begin_time))+"s")

            print("该文件夹存储完成.")

        # 全部存储结束断开连接
        save_data.close_connect()
        print("结束存储.")
        return 1

    # 处理数据
    # 参数:
    # ap_mac数组
    # x,y图大小    
    def data_process(self,ap_mac,c_x,c_y):
        d_process = DataProcess()
        dte = DataToExcel()
        for x in range(20):
            ap_m = d_process.process_data(ap_mac,x,c_x,c_y)
            # 写入方式1:写入到excel中
            # dte.dte(x,ap_mac,ap_m)
            
            #写入方式2:写入到数据库中
            flag = d_process.save_data(x,0,ap_mac,ap_m)
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
    # ####待完成方法
    def fingerprint_update(self,ap_mac,model_num,c_x,c_y):
        d_process = DataProcess()
        f_update = FingerprintUpdate(ap_mac)

        ditu = d_process.get_data(0,0,ap_mac[0],c_x,c_y)
        # 全部操作结束断开连接
        d_process.close_connect()
        data = []
        for x in range(len(ap_mac)):
            #d.get_median()
            #d.get_none()
            data.append(d.training())

        excel = DataToExcel()
        ##记得改文件名
        excel.odte("第一次增量学习结果",data,ap_mac)
        d.mlab_stop()
        return 1
    
g = GuiContent()
# g.save_data_event()
ap_mac = ('d8:15:0d:6c:13:98','00:90:4c:5f:00:2a','ec:17:2f:94:82:fc','70:ba:ef:d5:a6:12')
x = 10
y = 13
g.data_process(ap_mac,x,y)
# g.fingerprint_update(ap_mac,0,x,y)

