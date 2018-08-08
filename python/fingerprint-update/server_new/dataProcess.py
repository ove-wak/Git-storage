# 数据处理之连接数据库模块
import os,time
from connectMysql import ConnectMysql
from matching import Matching
class DataProcess:
    def __init__(self):
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()

    # 数据提取，预处理，保存指纹库
    # 
    def process_data(self,address,begin_time,end_time):
        ap_m = self.conn.select_data(address,begin_time,end_time)
        # 底图处理
        if end_time == global_begin_time: 
            #***与上一次底图进行比较，更新ap_mac（包含其中的无效化值）
        # 历史数据匹配
        else:
            #**历史数据匹配
            #
            match = Matching("信号类型0或1")
            # 匹配历史数据的时间范围
            match.history_division("开始时间", "结束时间")
            # 匹配的结果
            aps,result = match.match.history_matching(begin_time,end_time)
            #**两部分数据整合：ap_m和result
        return ap_m

    # 指纹库保存到数据库中
    # model_num模型序号，初始为0，每次底图采集递加1
    # update_num:更新次数,原数据更新次数为0,每次更新后更新次数加一并保存
    def save_data(self,attr,model_num,update_num,ap_mac,ap_m):
        signal_type = 1
        flag = self.conn.insert_fingerprint_data(model_num,update_num,addr,signal_type,ap_mac,ap_m)
        return flag

    # 获取指定指纹库
    # 
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