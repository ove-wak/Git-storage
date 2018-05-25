import os,time,csv
from connectMysql import ConnectMysql
class SaveData:
    def __init__(self):
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()

    # 完整数据保存               
    def data_save(self,path,type_t,addr,coo_x,coo_y): 
        if os.path.getsize(path):   
            with open(path, 'r') as file_read:           
                model = 0
                flag = 1
                line_datas = []
                read = csv.reader(file_read)
                for i in read:
                    line_datas.append(i)
                name = line_datas[0][1:]
                # print(name)
                mac = line_datas[1][1:]
                for x in range(2,len(line_datas)):
                    line_data = line_datas[x]
                    line_timet = line_data.pop(0)
                    line_time = line_timet[:-3]
                    line_time = time.strftime("%y-%m-%d %H:%M:%S",time.localtime(int(line_time)))
                    ap = line_data
                    flag_ap = -1
                    for a in ap:
                        if int(a) != -200:
                            flag_ap = 1
                    if flag_ap == 1:
                        flag = self.conn.insert_data(model,addr,type_t,coo_x,coo_y,line_time,mac,name,ap)  
                    if flag == -1:
                        return line_timet        
        return 1

    # 读取数据
    def data_read(self):
        data = self.conn.select_data()
        return data

    #关闭连接
    def close_connect(self):
        self.conn.close_conn()