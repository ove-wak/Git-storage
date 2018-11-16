import os,time,pymysql,json
from flask import Flask, request, g

app = Flask(__name__)


# 连接数据库
def connect_db():
    """Connects to the specific database."""
    rv = pymysql.connect(host="120.78.190.36",# 放到服务器上的最终版本记得修改为本地
                         port=3306,
                         user='invoice_root',
                         password='invoice_root',
                         db='invoice_db')
    return rv

# 初始化数据库,创建数据库等操作
def init_db():
    with app.app_context():
        db = connect_db()
        db.close()

# 每个请求单独建立sql连接
@app.before_request
def before_request():
    g.db = connect_db()

# 每个请求结束后关闭sql连接
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')#为下一行函数绑定url路径
def index():
    return 'index'

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    passwd = request.args.get('passwd')
    cursor = g.db.cursor()
    sql = "select id,permissionid from user where username='"+username+"' and password='"+passwd+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    if len(results) == 0:
        data = False
    else:
        data = {'userid':results[0][0],'permissionid':results[0][1]}
    return json.dumps({'data':data})

@app.route('/adduser', methods=['GET'])
def adduser():
    userid = request.args.get('userid')
    username = request.args.get('username')
    passwd = request.args.get('passwd')
    cursor = g.db.cursor()

    sql = "select * from user where username='"+username+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 用户已存在，返回false
        data = False
    else:
        sql = "insert into user values(NULL,'"+username+"','"+passwd+"',2);"
        flag = -1
        try:
            cursor.execute(sql)
            g.db.commit()
            flag = 1 # 添加用户成功
        except:
            g.db.rollback()
            flag = -1 
        cursor.close()
        if flag == 1:
            data = True
        else:
            data = False
    return json.dumps({'data':data})

if __name__ == '__main__': 
    # 初始化数据库
    init_db()
    # run 启动服务器
    # host='0.0.0.0' 设置为公网可访问(校园网内就是局域网)
    # debug 设置为调试模式:服务器会在代码修改后自动重新载入
    app.run(host='0.0.0.0',port=9601,debug=True)