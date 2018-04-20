import os,time
from connectMysql import ConnectMysql
class SaveData:
    # def __init__(self):
    #     # 连接数据库
    #     self.conn = ConnectMysql()
    #     # 如果表不存在则创建表
    #     self.conn.create_table()

    # 完整数据保存               
    def data_save(self,path,file,phone_model,tt_time): 
        print(path+"\n") 
        time_period = tt_time;
        with open(path + file, 'r') as file_read:
            file_a = file.split('.')
            file_b = file_a[0].split('-')
            addr = "C204"
            phoneIP = phone_model
            coordinate = file_b[1] # 注意x,y的先后
            strx = coordinate[len(coordinate) - 1]
            stry = coordinate[0:(len(coordinate) - 1)]
            direction = file_b[2]
            model = file_b[0]
            line_datas = []
            while True:
                lines = file_read.readline() # 读取整行数据
                if not lines:
                    break
                line_datas.append(lines.split())
            line_time_t = []
            for line_data in line_datas:
                line_time_t.append(line_data[0] + " " + line_data[1])
            for time_p in time_period:
                model = time_p[0]
                if time_p[1] in line_time_t and time_p[2] in line_time_t:
                    print(model+" " +str(1)) 
                    line_datas_t = line_datas[line_time_t.index(time_p[1]):line_time_t.index(time_p[2])]
                    if int(model) == 0: # 模型0为底图采集
                        for line_data in line_datas_t:
                            line_time = line_data.pop(0)
                            line_time = line_time + " " + line_data.pop(0)
                            mac = []
                            ap = []
                            if line_data:
                                for x in range(0,len(line_data),2):
                                    mac.append(line_data[x])
                                    ap.append(line_data[x+1])
                            # flag = self.conn.insert_data(model,addr,phoneIP,1,strx,stry,direction,line_time,mac,ap)  
                            # if flag == -1:
                            #     return line_time  
                    else: #其他数据分为四组
                        one = int(len(line_datas_t)/4)
                        for x in range(1,5):
                            o_line_datas = line_datas_t[one*(x-1):one*x]     
                            for line_data in o_line_datas:
                                line_time = line_data.pop(0)
                                line_time = line_time + " " + line_data.pop(0)
                                mac = []
                                ap = []
                                if line_data:
                                    for x in range(0,len(line_data),2):
                                        mac.append(line_data[x])
                                        ap.append(line_data[x+1])
                                # flag = self.conn.insert_data(str(x)+""+str(model),addr,phoneIP,1,strx,stry,direction,line_time,mac,ap)  
                                # if flag == -1:
                                #     return line_time 
        return 1

    # 读取数据
    def data_read(self):
        data = self.conn.select_data()
        return data

    #关闭连接
    def close_connect(self):
        pass
        # self.conn.close_conn()

