import pymysql

# 连接数据库
def connect(self):
    db = pymysql.connect(host="localhost",
                         port=3306,
                         user='root',
                         password='123456',
                         db='test_database')
    return db

# 关闭数据库连接
def close_conn(self,db):
    db.close()

# 创建表
def create_table(self,db):
    cursor = db.cursor()
    # 创建指纹记录表
    sql = """CREATE TABLE IF NOT EXISTS fingerprint_record(
             id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
             phone_ip CHAR(15) NOT NULL,
             signal_type INT NOT NULL,
             coordinate_x INT NOT NULL,
             coordinate_y INT NOT NULL,
             signal_time VARCHAR(40))
             """
    cursor.execute(sql)
    # 创建信号记录表
    sql = """CREATE TABLE IF NOT EXISTS signal_record(
             id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
             record_id INT UNSIGNED NOT NULL,
             signal_mac_address VARCHAR(20),
             signal_strength INT NOT NULL)
             """
    cursor.execute(sql)
    cursor.close()

# 删除表
def drop_table(self,db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS fingerprint_record")
    cursor.execute("DROP TABLE IF EXISTS signal_record")
    cursor.close()

# 插入数据
def insert_data(self,db):
    cursor = db.cursor()
    #
    #
    #
    sql = ""
    flag = 0 # 是否执行成功标记
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        flag = 1
    except:
        # 如果发生错误则回滚
        db.rollback()
        flag = -1
    cursor.close()
    return flag

# 查询数据
def select_data(self,db):
    cursor = db.cursor()
    #
    #
    #
    sql = ""
    flag = 0 # 是否执行成功标记
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        flag = 1
    except:
        # 如果发生错误则回滚
        db.rollback()
        flag = -1
    cursor.close()
    return flag

# 更新数据
def update_data(self,db):
    cursor = db.cursor()
    #
    #
    #
    sql = ""
    flag = 0 # 是否执行成功标记
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        flag = 1
    except:
        # 如果发生错误则回滚
        db.rollback()
        flag = -1
    cursor.close()
    return flag

# 删除数据
def delete_data(self,db):
    cursor = db.cursor()
    #
    #
    #
    sql = ""
    flag = 0 # 是否执行成功标记
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        flag = 1
    except:
        # 如果发生错误则回滚
        db.rollback()
        flag = -1
    cursor.close()
    return flag

