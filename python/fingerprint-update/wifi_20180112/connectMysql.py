import pymysql
import xlwt,time
import matplotlib.pyplot as plt

class ConnectMysql:
    # 初始化类连接数据库
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                             port=3306,
                             user='root',
                             password='123456',
                             db='wifi_test')

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
        cursor.close()

    # 删除表
    def drop_table(self):
        cursor = self.db.cursor()
        cursor.execute("DROP TABLE IF EXISTS fingerprint_record")
        cursor.execute("DROP TABLE IF EXISTS signal_record")
        cursor.close()

    # 插入数据
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

# 预处理得到后续数据excel文件
    def select_data(self,model_num):
        num = 0
        ap_mac = ('d8:15:0d:6c:13:98','00:90:4c:5f:00:2a','ec:17:2f:94:82:fc','70:ba:ef:d5:a6:12')
        data = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0]]

        cursor = self.db.cursor()
        sql = "select id,coordinate_x,coordinate_y from fingerprint_record where model_num="+str(model_num)+";"
        cursor.execute(sql)    
        results=cursor.fetchall()
        results = list(results)
        for result in results:
            if data[result[1]][result[2]] == 0:
                data[result[1]][result[2]] = []
            data[result[1]][result[2]].append(result[0])
        for x in range(len(data)):
            for y in range(len(data[0])):
                if data[x][y] != 0:
                    temp = data[x][y]
                    data[x][y] = []
                    for mac in ap_mac:
                        sql = "select signal_strength from signal_record where record_id IN "+str(tuple(temp))+" and signal_mac_address='"+mac+"';" 
                        cursor.execute(sql)
                        res=cursor.fetchall()
                        num = 0
                        for r in res:
                            num = num + r[0]
                        if len(res) == 0:
                            data[x][y].append(-95)
                        else:
                            data[x][y].append(int(num/len(res)))####重点,目前取得是平均值,可优化
        dte = DataToExcel()
        dte.dte(model_num,data)
        cursor.close()
        return 1

    # 数据处理得到图像查看数据的稳定性//发现人越多越不稳定
    def img_data(self):
        begin_time = time.time()
        num = 0
        ap_mac = ('ec:88:8f:b3:4a:d0','d0:c7:c0:0b:d2:88','20:6b:e7:a3:1d:29','0a:69:6c:bc:f7:4d')
        # ap_mac = ['d8:15:0d:6c:13:98']
        cursor = self.db.cursor()
        sql = "select id from fingerprint_record where model_num=98 and coordinate_x=0000 and coordinate_y=0000;"
        cursor.execute(sql)    
        results=cursor.fetchall()
        plt.figure(1)
        x = []
        z = []
        for ap in ap_mac:
            x = []
            y = []
            for result in results:
                x.append(result[0])
                sql = "select signal_strength from signal_record where record_id = "+str(result[0])+" and signal_mac_address = '"+ap+"';" 
                cursor.execute(sql)
                res=cursor.fetchall()
                if res != ():
                    y.append(res[0][0])
                else:
                    y.append(-50)
                print(result[0])
            z.append(y)
        plt.scatter(x,z[0],c = 'r')
        plt.scatter(x,z[1],c = 'y') 
        plt.scatter(x,z[2],c = 'g') 
        plt.scatter(x,z[3],c = 'b')        
        end_time = time.time()
        print("time=" + str(end_time-begin_time))
        plt.show()               
        cursor.close()
        return 1

    # 预处理得到底图
    def select_data_basemap(self):
        num = 0
        ap_mac = ('d8:15:0d:6c:13:98','00:90:4c:5f:00:2a','ec:17:2f:94:82:fc','70:ba:ef:d5:a6:12')
        ditu = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0]]

        cursor = self.db.cursor()
        sql = "select id,coordinate_x,coordinate_y from fingerprint_record where model_num=0;"
        cursor.execute(sql)    
        results=cursor.fetchall()
        results = list(results)
        for result in results:
            if ditu[result[1]][result[2]] == 0:
                ditu[result[1]][result[2]] = []
            ditu[result[1]][result[2]].append(result[0])
        for x in range(len(ditu)):
            for y in range(len(ditu[0])):
                if ditu[x][y] != 0:
                    temp = ditu[x][y]
                    ditu[x][y] = []
                    for mac in ap_mac:
                        sql = "select signal_strength from signal_record where record_id IN "+str(tuple(temp))+" and signal_mac_address='"+mac+"';" 
                        cursor.execute(sql)
                        res=cursor.fetchall()
                        num = 0
                        for r in res:
                            num = num + r[0]
                        ditu[x][y].append(int(num/len(res)))
                    print(ditu[x][y]) 
        print(ditu)# 处理得到底图原始数据,在 底图.py 文件里进行插值并保存为excel得到完整底图
        cursor.close()
        return 1

# 测试环境下运行
if __name__ == "__main__":
    conn = ConnectMysql()
    conn.img_data()
    #conn.drop_table()
    # for x in range(1,20):
    #     conn.select_data(x)
    #     print(str(x)+" complete")

