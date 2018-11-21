import pymysql,json

g_host = ""
g_port = ""
g_user = ""
g_password = ""
g_db = ""
g_range = ""

with open("config.json", 'r',encoding='UTF-8') as file_read:
    results = json.load(file_read)
    g_host = results["host"]# 放到服务器上的最终版本记得修改为本地
    g_port = results["port"]
    g_user = results["user"]
    g_password = results["password"]
    g_db = results["db"]
    g_range = results["compliance_range"]

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
         manager VARCHAR(60) NOT NULL) DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
sql = """CREATE TABLE IF NOT EXISTS invoice(
         id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
         userid INT NOT NULL,
         versionid INT NOT NULL,
         invoicecode VARCHAR(20) NOT NULL,
         invoicenumber VARCHAR(10) NOT NULL,  
         remarks VARCHAR(120)) DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
db.close()