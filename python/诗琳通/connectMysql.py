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

if __name__ == '__main__':
    conn = ConnectMysql()
    # conn.drop_table()
