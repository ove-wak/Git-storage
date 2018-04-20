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
        time_period = [];
        with open(path + file, 'r') as file_read:
            file_a = file.split('.')
            file_b = file_a[0].split('-')
            addr = "C204"
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
            time_period.append(model)
            first_line = line_datas[0]
            last_line = line_datas[-1]
            time_period.append(first_line.pop(0) + " " + first_line.pop(0))
            time_period.append(last_line.pop(0) + " " + last_line.pop(0))
            if int(model) == 0: # 模型0为底图采集
                for line_data in line_datas:
                    line_time = line_data.pop(0)
                    line_time = line_time + " " + line_data.pop(0)
                    mac = []
                    ap = []
                    if line_data:
                        for x in range(0,len(line_data),2):
                            mac.append(line_data[x])
                            ap.append(line_data[x+1])
                    flag = self.conn.insert_data(model,addr,phoneIP,1,strx,stry,direction,line_time,mac,ap)  
                    if flag == -1:
                        return line_time  
            else: #其他数据分为四组
                one = int(len(line_datas)/4)
                for x in range(1,5):
                    o_line_datas = line_datas[one*(x-1):one*x]     
                    for line_data in o_line_datas:
                        line_time = line_data.pop(0)
                        line_time = line_time + " " + line_data.pop(0)
                        mac = []
                        ap = []
                        if line_data:
                            for x in range(0,len(line_data),2):
                                mac.append(line_data[x])
                                ap.append(line_data[x+1])
                        flag = self.conn.insert_data(str(x)+""+str(model),addr,phoneIP,1,strx,stry,direction,line_time,mac,ap)  
                        if flag == -1:
                            return line_time 
        return time_period

    # 读取数据
    def data_read(self):
        data = self.conn.select_data()
        return data

    #关闭连接
    def close_connect(self):
        self.conn.close_conn()