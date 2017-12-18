import os,time
from connectMysql import ConnectMysql
class SaveData:
    def __init__(self):
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()

    # 完整数据保存               
    def complete_data_save(self,path,file):    
        with open(path + file, 'r') as file_read:
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
                    return line_time        
        return 1

    #底图数据,只保存中间三分之一
    def initial_data_save(self,path,file):
        with open(path + file, 'r') as file_read:
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
                    return line_time     
        return 1

    def close_connect(self):
        self.conn.close_conn()