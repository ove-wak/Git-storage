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
                 address VARCHAR(20) NOT NULL,\
                 phone_ip CHAR(15) NOT NULL,\
                 signal_type INT NOT NULL,\
                 coordinate_x INT NOT NULL,\
                 coordinate_y INT NOT NULL,\
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
    def insert_data(self,addr,phoneIP,strtype,x,y,time,mac,ap):
        cursor = self.db.cursor()
        sql = "INSERT INTO fingerprint_record VALUES(NULL, '" + addr + "', '" + phoneIP + "', " + str(strtype) + ", " + str(x) + ", " + str(y) + ", '" + time + "');"
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

    # 查询数据**待完成
    def select_data(self):
        cursor = self.db.cursor()
        #
        #
        #
        sql = ""
        flag = 0 # 是否执行成功标记
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
        cursor.close()
        return flag

    # 更新数据
    # *暂不需要
    def update_data(self):
        cursor = self.db.cursor()
        #
        #
        #
        sql = ""
        flag = 0 # 是否执行成功标记
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
        cursor.close()
        return flag

    # 删除数据
    # *暂不需要
    def delete_data(self):
        cursor = self.db.cursor()
        #
        #
        #
        sql = ""
        flag = 0 # 是否执行成功标记
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
        cursor.close()
        return flag

    # 数据处理得到图像查看数据的稳定性//发现人越多越不稳定
    def img_data(self):
        begin_time = time.time()
        num = 0
        ap_mac = ('a6:44:d1:3f:4f:97','00:24:6c:c4:ec:80','00:24:6c:c4:ee:40','00:24:6c:c4:ec:90')
        # ap_mac = ['d8:15:0d:6c:13:98']
        cursor = self.db.cursor()
        sql = "select id from fingerprint_record where coordinate_x=2 and coordinate_y=3;"
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
                    y.append(-95)
            z.append(y)
        plt.scatter(x,z[0],s=1,c = 'r')
        plt.scatter(x,z[1],s=1,c = 'y') 
        plt.scatter(x,z[2],s=1,c = 'g') 
        plt.scatter(x,z[3],s=1,c = 'b')        
        end_time = time.time()
        print("time=" + str(end_time-begin_time))
        plt.show()               
        cursor.close()
        return 1
# 测试环境下运行
if __name__ == "__main__":
    conn = ConnectMysql()
    # for x in range(2,20):
    #     conn.select_data(x)
    #     print(str(x)+" complete")
    conn.img_data()