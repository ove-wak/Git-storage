# 核心数据库模块
import pymysql
import xlwt,time,numpy
import matplotlib.pyplot as plt

class ConnectMysql:
    # 初始化类连接数据库
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                             port=3306,
                             user='root',
                             password='123456',
                             db='wifi_db')

    # 关闭连接
    def close_conn(self):
        self.db.close()
    
    # 创建表
    # 对于没有 phone_ip 的数据,人为标识区分
    def create_table(self):
        cursor = self.db.cursor()
        # 创建指纹记录表
        sql = "CREATE TABLE IF NOT EXISTS fingerprint_record(\
                 id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                 model_num INT NOT NULL,\
                 address VARCHAR(20) NOT NULL,\
                 phone_ip VARCHAR(20) NOT NULL,\
                 signal_type INT NOT NULL,\
                 coordinate_x INT NOT NULL,\
                 coordinate_y INT NOT NULL,\
                 direction VARCHAR(6),\
                 signal_time VARCHAR(40));"
        cursor.execute(sql)
        # 创建信号记录表
        sql = "CREATE TABLE IF NOT EXISTS signal_record(\
                 id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                 record_id INT UNSIGNED NOT NULL,\
                 signal_mac_address VARCHAR(20),\
                 signal_strength INT NOT NULL);"
        cursor.execute(sql)
        # 创建指纹库表
        sql = "CREATE TABLE IF NOT EXISTS fingerprint_lib(\
                 id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                 model_num INT NOT NULL,\
                 update_num INT NOT NULL,\
                 address VARCHAR(20) NOT NULL,\
                 signal_type INT NOT NULL,\
                 coordinate_x INT NOT NULL,\
                 coordinate_y INT NOT NULL,\
                 signal_mac_address VARCHAR(20),\
                 signal_strength INT NOT NULL);"
        cursor.execute(sql)
        cursor.close()

    # 删除表
    def drop_table(self):
        cursor = self.db.cursor()
        cursor.execute("DROP TABLE IF EXISTS fingerprint_record")
        cursor.execute("DROP TABLE IF EXISTS signal_record")
        cursor.close()

    # 插入指纹信号数据
    def insert_data(self,model,addr,phoneIP,strtype,x,y,direction,time,mac,ap):
        cursor = self.db.cursor()
        sql = "INSERT INTO fingerprint_record VALUES(NULL, '" + str(model) + "', '" + addr + "', '" + phoneIP + "', " + str(strtype) + ", " + str(x) + ", " + str(y) + ", '" + direction + "', '" + time + "');"
        flag = 0 # 是否执行成功标记
        try:
            # 执行sql语句
            cursor.execute(sql)
            flag = 1
            strRecordID = str(cursor.lastrowid)
            if mac:
                strsql = []
                for i in range(len(mac)):
                    strsql.append("(NULL, " + strRecordID + ", '" + mac[i] + "', " + str(ap[i]) + ")")
                sql ="INSERT INTO signal_record VALUES" + ",".join(strsql) + ";"  
                try:
                    cursor.execute(sql)
                    flag = 1  
                except:
                    self.db.rollback()
                    flag = -1 

            # 提交到数据库执行
            self.db.commit()   
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            flag = -1
        cursor.close()
        return flag

    # 读取原始指纹库
    def select_data(self,ap_mac,model_num,c_x,c_y):
        #初始化数组
        ap_m = []
        for i in range(len(ap_mac)):
            ap_m.append([])
            for j in range(c_x):
                ap_m[i].append([])
                for k in range(c_y):
                    ap_m[i][j].append(-1)
        mid_data = []
        for i in range(c_x):
            mid_data.append([])
            for j in range(c_y):
                mid_data[i].append(-1)

        cursor = self.db.cursor()
        sql = "select id,coordinate_x,coordinate_y from fingerprint_record where model_num="+str(model_num)+";"
        cursor.execute(sql)    
        results=cursor.fetchall()
        results = list(results)
        for result in results:
            if mid_data[result[1]][result[2]] == -1:
                mid_data[result[1]][result[2]] = []
            mid_data[result[1]][result[2]].append(result[0])
        for x in range(c_x):
            for y in range(c_y):
                if mid_data[x][y] != -1:
                    for ap in range(len(ap_mac)):
                        sql = "select signal_strength from signal_record where record_id IN "+str(tuple(mid_data[x][y]))+" and signal_mac_address='"+ap_mac[ap]+"';" 
                        cursor.execute(sql)
                        res=cursor.fetchall()
                        num = 0
                        for r in res:
                            num = num + r[0]
                        if len(res) == 0:
                           ap_m[ap][x][y] = -95
                        else: 
                            ap_m[ap][x][y] = int(num/len(res))###目前直接取均值
                        ####计算标准差
                        # num = []
                        # for r in res:
                        #     num.append(r[0])
                        # if len(res) == 0:
                        #     ap_m[ap][x][y] = -100
                        # else:
                        #     ap_m[ap][x][y] = numpy.std(num)
        cursor.close()
        return ap_m

    # 插入指纹库数据
    def insert_fingerprint_data(self,model_num,update_num,addr,signal_type,ap_mac,ap_m):
        cursor = self.db.cursor()
        flag = 0 # 是否执行成功标记
        for t in range(len(ap_mac)):  
            for x in range(len(ap_m[0])):
                for y in range(len(ap_m[0][0])):
                    sql = "INSERT INTO fingerprint_lib VALUES(NULL, " + str(model_num) + ", " + str(update_num) + ", '" + addr + "', " + str(signal_type) + ", " + str(x) + ", " + str(y) + ", '" + ap_mac[t] + "', " + str(ap_m[t][x][y]) + ");"    
                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 提交到数据库执行
                        self.db.commit() 
                        flag = 1
                    except:
                        # 如果发生错误则回滚
                        self.db.rollback()
                        flag = -1
                        return flag      
        cursor.close()
        return flag

    # 读取指纹库数据
    def select_fingerprint_data(self,model_num,update_num,signal_mac_address):
        cursor = self.db.cursor()
        sql = "select coordinate_x,coordinate_y,signal_strength from fingerprint_lib where model_num="+str(model_num)+" and update_num="+str(update_num)+" and signal_mac_address='"+signal_mac_address+"';"
        cursor.execute(sql)    
        results=cursor.fetchall()
        results = list(results)
        return results

        