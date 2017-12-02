import os,time
from connectMysql import ConnectMysql
class SaveData:
    def __init__(self,path):
        self.path = path
        self.file_name = []
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()
        # 获取指定目录下所有数据的文件名
        tt = os.walk(self.path)
        for i in tt:
            for j in i[2]:
                if ".txt" in j:
                    self.file_name.append(j)

    # 完整数据保存               
    def complete_data_save(self,text):    
        self.show_text = "目录" + self.path + " 下的文件正在存储\n"
        text.set(self.show_text)
        # 遍历指定目录下所有数据文件并插入到数据库中
        for file in self.file_name:
            begin_time = time.time()
            self.show_text = self.show_text + file + " saving...\n"
            text.set(self.show_text)
            with open(self.path + file, 'r') as file_read:
                file_a = file.split('.')
                file_b = file_a[0].split('-')
                addr = file_b[0]
                strx = file_b[1] # 注意x,y的先后
                stry = file_b[2]
                phoneIP = strx + ', ' +stry # ##phoneIP为采集中缺失的参数,暂时用位置和代替
                while True:
                    lines = file_read.readline() # 读取整行数据
                    if not lines:
                        break
                    line_data = lines.split()
                    line_time = line_data.pop(0)
                    line_time = line_time + " " + line_data.pop(0)
                    mac = []
                    ap = []
                    if line_data:
                        for x in range(0,len(line_data),2):
                            mac.append(line_data[x])
                            ap.append(line_data[x+1])
                    flag = self.conn.insert_data(addr,phoneIP,1,strx,stry,line_time,mac,ap)  
                    if flag == -1:
                        self.show_text = self.show_text + "数据库插入数据出错\n"
                        self.show_text = self.show_text + "出错位置:" + file+" "+lines
                        text.set(self.show_text)
                        return -1 
            end_time = time.time()      
            self.show_text = self.show_text + file + " saved,time:"+str(int(end_time-begin_time))+"s\n"
            text.set(self.show_text)       

        self.conn.close_conn()
        return 1


    #底图数据,只保存中间三分之一
    def initial_data_save(self,text):
        self.show_text = "目录:" + self.path + "下的文件正在存储\n"
        text.set(self.show_text)
        # 遍历指定目录下所有数据文件并插入到数据库中
        for file in self.file_name:
            begin_time = time.time()
            self.show_text = self.show_text + file + "saving...\n"
            text.set(self.show_text)
            with open(self.path + file, 'r') as file_read:
                file_a = file.split('.')
                file_b = file_a[0].split('-')
                addr = file_b[0]
                strx = file_b[1] # 注意x,y的先后
                stry = file_b[2]
                phoneIP = strx + ', ' +stry # ##phoneIP为采集中缺失的参数,暂时用位置和代替
                line_datas = []
                while True:
                    lines = file_read.readline() # 读取整行数据
                    if not lines:
                        break
                    line_datas.append(lines.split())
                one = int(len(line_datas)/3)
                line_datas = line_datas[one:one*2]
                for line_data in line_datas:
                    line_time = line_data.pop(0)
                    line_time = line_time + " " + line_data.pop(0)
                    mac = []
                    ap = []
                    if line_data:
                        for x in range(0,len(line_data),2):
                            mac.append(line_data[x])
                            ap.append(line_data[x+1])
                    flag = self.conn.insert_data(addr,phoneIP,1,strx,stry,line_time,mac,ap)  
                    if flag == -1:
                        self.show_text = self.show_text + "数据库插入数据出错\n"
                        self.show_text = self.show_text + "出错位置:" + file+" "+lines
                        text.set(self.show_text)
                        return -1 

            end_time = time.time()      
            self.show_text = self.show_text + file + " saved,time:"+str(int(end_time-begin_time))+"s\n"
            text.set(self.show_text)        

        self.conn.close_conn()
        self.show_text = self.show_text + "存储完成."
        text.set(self.show_text)
        return 1