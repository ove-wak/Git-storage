import pymysql,json

g_host = ""
g_port = ""
g_user = ""
g_password = ""
g_db = ""

with open("config.json", 'r',encoding='UTF-8') as file_read:
    results = json.load(file_read)
    g_host = results["host"]
    g_port = results["port"]
    g_user = results["user"]
    g_password = results["password"]
    g_db = results["db"]

# 连接数据库
def connect_db():
    """Connects to the specific database."""
    rv = pymysql.connect(host=g_host,
                         port=g_port,
                         user=g_user,
                         password=g_password,
                         db=g_db,
                         charset='utf8')
    return rv

db = connect_db()
cursor = db.cursor()
sql = """CREATE TABLE IF NOT EXISTS rule(
         id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         rulerange INT NOT NULL) DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
sql = """CREATE TABLE IF NOT EXISTS user(
         id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(40) NOT NULL,
         password VARCHAR(40) NOT NULL,  
         permissionid INT NOT NULL) DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
sql = """CREATE TABLE IF NOT EXISTS version(
         id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         userid INT NOT NULL,
         date VARCHAR(10) NOT NULL,
         department VARCHAR(60) NOT NULL,  
         serialnumber VARCHAR(60) NOT NULL,
         manager VARCHAR(60) NOT NULL,
         totalnumber INT NOT NULL,
         completednumber INT NOT NULL) DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
sql = """CREATE TABLE IF NOT EXISTS invoice(
         id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         userid INT NOT NULL,
         versionid INT NOT NULL,
         invoicecode VARCHAR(20) NOT NULL,
         invoicenumber VARCHAR(10) NOT NULL,  
         remarks VARCHAR(120),
         queuenumber INT NOT NULL) DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
sql = "insert into user values(NULL,'admin','invoice_root',1);"
flag = -1
try:
    cursor.execute(sql)
    db.commit()
    flag = 1 # 添加用户成功
except:
    db.rollback()
    flag = -1
print(flag)
sql = "insert into rule values(NULL,1);"
flag = -1
try:
    cursor.execute(sql)
    db.commit()
    flag = 1 # 添加规则成功
except:
    db.rollback()
    flag = -1
print(flag)
db.close()
