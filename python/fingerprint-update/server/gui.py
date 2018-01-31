# 暂时读取本地txt文件并保存
import os,time
from saveData import SaveData

class GuiContent:    
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
    
g = GuiContent()
g.save_data_event()
