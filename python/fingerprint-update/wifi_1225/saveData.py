import os,time
from connectMysql import ConnectMysql
class SaveData:
    def __init__(self):
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()

    # 完整数据保存               
    def data_save(self,path,file,phone_model):    
        with open(path + file, 'r') as file_read:
            file_a = file.split('.')
            file_b = file_a[0].split('-')
            addr = "701"
            phoneIP = phone_model
            model = file_b[0]
            coordinate = file_b[1] # 注意x,y的先后
            strx = coordinate[len(coordinate) - 1]
            stry = coordinate[0:(len(coordinate) - 1)]
            direction = file_b[2]
            line_datas = []
            while True:
                lines = file_read.readline() # 读取整行数据
                if not lines:
                    break
                line_datas.append(lines.split())
            if int(model) == 0: # 模型0为底图采集,只保存中间三分之一数据 
                one = int(len(line_datas)/3)
                line_datas = line_datas[one:one*2]
            for line_data in line_datas:
                line_time = line_data.pop(0)
                line_time = line_time + " " + line_data.pop(0)
                mac = []
                ap = []
                if line_data:
                    for x in range(0,len(line_data),2):
                        if int(line_data[x+1]) > -70:
                            mac.append(line_data[x])
                            ap.append(line_data[x+1])
                flag = self.conn.insert_data(model,addr,phoneIP,1,strx,stry,direction,line_time,mac,ap)  
                if flag == -1:
                    return line_time        
        return 1

    # 读取数据
    def data_read(self):
        data = self.conn.select_data()
        return data

    #关闭连接
    def close_connect(self):
        self.conn.close_conn()