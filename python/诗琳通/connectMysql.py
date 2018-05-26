import pymysql
import xlwt,time,numpy,json
import matplotlib.pyplot as plt

class ConnectMysql:
    # 初始化类连接数据库
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                             port=3306,
                             user='root',
                             password='123456',
                             db='shilintong_db')

    # 关闭连接
    def close_conn(self):
        self.db.close()
    
    # 创建表
    # 对于没有 phone_ip 的数据,人为标识区分
    def create_table(self):
        cursor = self.db.cursor()
        # 创建指纹记录表
        # x,y 浮点数和字符串哪个存储效率高?
        sql = "CREATE TABLE IF NOT EXISTS fingerprint_record(\
                 id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                 model_num INT NOT NULL,\
                 address VARCHAR(20) NOT NULL,\
                 signal_type INT NOT NULL,\
                 coordinate_x VARCHAR(20) NOT NULL,\
                 coordinate_y VARCHAR(20) NOT NULL,\
                 signal_time VARCHAR(40));"
        cursor.execute(sql)
        # 创建信号记录表
        sql = "CREATE TABLE IF NOT EXISTS signal_record(\
                 id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                 record_id INT UNSIGNED NOT NULL,\
                 signal_mac_address VARCHAR(20),\
                 signal_name VARCHAR(40),\
                 signal_strength INT NOT NULL);"
        cursor.execute(sql)
        cursor.close()

    # 删除表
    def drop_table(self):
        cursor = self.db.cursor()
        cursor.execute("DROP TABLE IF EXISTS fingerprint_record")
        cursor.execute("DROP TABLE IF EXISTS signal_record")
        cursor.close()

    # 插入数据
    def insert_data(self,model,addr,strtype,x,y,time,mac,name,ap):
        cursor = self.db.cursor()
        sql = "INSERT INTO fingerprint_record VALUES(NULL, '" + str(model) + "', '" + addr + "', " + str(strtype) + ", '" + str(x) + "', '" + str(y) + "', '" + time + "');"
        flag = 0 # 是否执行成功标记
        try:
            # 执行sql语句
            cursor.execute(sql)
            flag = 1
            strRecordID = str(cursor.lastrowid)
            strsql = []
            for i in range(len(mac)):
                if int(ap[i]) != -200:
                    if name[i] == "null":
                        name[i] = ""
                    # print(name[i])
                    strsql.append("(NULL, " + strRecordID + ", '" + mac[i] + "', '" + name[i] + "', " + str(ap[i]) + ")")
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

    #读取数据库并保存为指定json格式
    ### 对比之后发现两个问题:
    #1.当前绝对坐标跟经纬度的区别
    #2.字典和json参数的顺序问题??
    def read_data(self,signal_type):

        record = {}
        temp = -1
        ap = 0       
        cursor = self.db.cursor()
        sql = "select * from signal_record;" 
        cursor.execute(sql)
        res=cursor.fetchall()
        for r in res:
            if r[1] == temp:
                ap = ap + 1
                record[r[1]].append({'AP':ap,'BSSID':r[2],'SSID':r[3],'Level':r[4]})
            else:
                ap = 0
                temp = r[1]
                record[r[1]] = [{'AP':ap,'BSSID':r[2],'SSID':r[3],'Level':r[4]}]


        data = []
        pt = 0
        c_x = ""
        c_y = ""
        point_num = 0
        round_num = 1
        sql = "select * from fingerprint_record where signal_type = "+str(signal_type)+";"
        cursor.execute(sql)    
        results=cursor.fetchall()
        results = list(results)
        for result in results:
            scaninfo = record[result[0]]
            if result[4] == c_x and result[5] == c_y:
                round_num = round_num + 1
                pt['WIFIscan'].append({'Round':round_num,'Date':result[6],'WifiScanInfo':scaninfo})
            else:
                round_num = 1
                c_x = result[4]
                c_y = result[5]
                if pt != 0:
                    data.append(pt)
                pt = {}
                pt['Point NO'] = point_num
                pt['PosLon'] = float(c_x)
                pt['PosLat'] = float(c_y)
                pt['Building ID'] = 'shilintong'
                pt['Floor ID'] = str(result[2][10:12])
                pt['Date'] = result[6]
                pt['WIFIscan'] = [{'Round':round_num,'Date':result[6],'WifiScanInfo':scaninfo}]
                point_num = point_num + 1           
        cursor.close()
        return data

if __name__ == '__main__':
    conn = ConnectMysql()
    # conn.drop_table()
    signal_type = 1# 1为wifi;2为蓝牙
    data = conn.read_data(signal_type)
    if signal_type == 1:
        with open('shilintong_wifi.json', 'w') as f:
            json.dump(data, f)
    else:
        with open('shilintong_bt.json', 'w') as f:
            json.dump(data, f)
