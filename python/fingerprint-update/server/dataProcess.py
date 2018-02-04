# 数据处理之连接数据库模块
import os,time
from connectMysql import ConnectMysql
class DataProcess:
    def __init__(self):
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()

    # 数据处理
    def process_data(self,ap_mac,model_num,c_x,c_y):
        ap_m = self.conn.select_data(ap_mac,model_num,c_x,c_y)
        # c204底图数据额外处理
        if model_num == 0:
            for t in range(len(ap_mac)):
                for x in range(c_x):
                    for y in range(c_y):
                        if x == 0 or x == 1 or x == 9 or y == 0 or y == 12:
                            pass
                        elif ap_m[t][x][y] != -1:
                            pass
                        elif (x % 2) == 1 and (y % 2) == 1:
                            ap_m[t][x][y] = int((ap_m[t][x-1][y]+ap_m[t][x+1][y])/2)
                        elif (x % 2) == 1 and (y % 2) == 0:
                            ap_m[t][x][y] = int((ap_m[t][x-1][y-1]+ap_m[t][x-1][y+1]+ap_m[t][x+1][y-1]+ap_m[t][x+1][y+1])/4)
                        else:
                            ap_m[t][x][y] = int((ap_m[t][x][y-1]+ap_m[t][x][y+1])/2)
        return ap_m

    # 指纹库保存到数据库中
    # update_num:更新次数,原数据更新次数为0,每次更新后更新次数加一并保存
    def save_data(self,model_num,update_num,ap_mac,ap_m):
        addr = "c204"
        signal_type = 1
        flag = self.conn.insert_fingerprint_data(model_num,update_num,addr,signal_type,ap_mac,ap_m)
        return flag

    # 获取指定指纹库
    def get_data(self,model_num,update_num,signal_mac_address,c_x,c_y):
        results = self.conn.select_fingerprint_data(model_num,update_num,signal_mac_address)        
        mid_data = []
        for i in range(c_x):
            mid_data.append([])
            for j in range(c_y):
                mid_data[i].append(-1)
        for r in results:
            mid_data[r[0]][r[1]] = r[2]
        return mid_data

    
    #关闭连接
    def close_connect(self):
        self.conn.close_conn()