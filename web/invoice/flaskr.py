import os,time,pymysql,json
from flask import Flask, request, g

g_host = ""
g_port = ""
g_user = ""
g_password = ""
g_db = ""
with open("config.json", 'r',encoding='UTF-8') as file_read:
    results = json.load(file_read)
    g_host = results["host"]# 放到服务器上的最终版本记得修改为本地
    g_port = results["port"]
    g_user = results["user"]
    g_password = results["password"]
    g_db = results["db"]


app = Flask(__name__)

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
    password = request.args.get('password')
    cursor = g.db.cursor()
    sql = "select id,permissionid from user where username='"+username+"' and password='"+password+"';" 
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
    password = request.args.get('password')
    cursor = g.db.cursor()

    sql = "select * from user where username='"+username+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 用户已存在，返回false
        data = False
    else:
        sql = "insert into user values(NULL,'"+username+"','"+password+"',2);"
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

@app.route('/deleteuser', methods=['GET'])
def deleteuser():
    userid = request.args.get('userid')
    bedeletedid = request.args.get('bedeletedid')
    cursor = g.db.cursor()
    if userid != bedeletedid:
        sql = "delete from user where id='"+bedeletedid+"';"
        flag = -1
        try:
            cursor.execute(sql)
            g.db.commit()
            flag = 1 # 删除用户成功
        except:
            g.db.rollback()
            flag = -1 
        cursor.close()
        if flag == 1:
            data = True
        else:
            data = False
    else:
        data = False
    return json.dumps({'data':data})

@app.route('/changeuser', methods=['GET'])
def changeuser():
    userid = request.args.get('userid')
    bechangedid = request.args.get('bechangedid')
    username = request.args.get('username')
    password = request.args.get('password')
    cursor = g.db.cursor()

    sql = "select * from user where id='"+bechangedid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 用户存在
        sql = "update user set password='"+password+"' where id='"+bechangedid+"';"
        flag = -1
        try:
            cursor.execute(sql)
            g.db.commit()
            flag = 1 # 更新用户成功
        except:
            g.db.rollback()
            flag = -1 
        cursor.close()
        if flag == 1:
            data = True
        else:
            data = False
    else:
        data = False
    return json.dumps({'data':data})

@app.route('/begin', methods=['GET'])
def begin():
    userid = request.args.get('userid')
    date = request.args.get('date')
    department = request.args.get('department')
    serialnumber = request.args.get('serialnumber')
    manager = request.args.get('manager')
    totalnumber = request.args.get('totalnumber')
    cursor = g.db.cursor()

    sql = "select * from user where id='"+userid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 用户存在
        sql = "select * from version where serialnumber='"+serialnumber+"';" 
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:#全新的版本
            sql = "insert into version values(NULL,"+userid+",'"+date+"','"+department+"','"+serialnumber+"','"+manager+"',"+totalnumber+",0);"
            flag = -1
            try:
                cursor.execute(sql)
                g.db.commit()
                sql = "select last_insert_id();" 
                cursor.execute(sql) 
                results = cursor.fetchall()
                flag = 1 # 添加版本成功
            except:
                g.db.rollback()
                flag = -1 
        
            if flag == 1:
                data = {"flag":1,"versionid":results[0][0]}
            else:
                data = False
        else:# 已经存在的版本
            versionid = results[0][0]
            totalnumber = int(totalnumber)
            if totalnumber != results[0][6]:
                if totalnumber <= results[0][7]:
                    data = {"flag":-1,"message":"本版此次输入的总张数小于已识别张数，不合法"}
                else:
                    data = {"flag":2,"message":"本版此次输入的总张数与上次("+str(results[0][6])+")不一致，确认继续么？"}
            else:
                if totalnumber == results[0][7]:
                    data = {"flag":-1,"message":"本版已检测完成"}
                else:
                    data = {"flag":3,"message":"本版已检测完成前"+str(results[0][7])+"张","completednumber":results[0][7],"versionid":versionid}
    else:
        data = False
    cursor.close()
    return json.dumps({'data':data}, ensure_ascii=False)

# 张数不一致时确认继续
@app.route('/conbegin', methods=['GET'])
def conbegin():
    userid = request.args.get('userid')
    date = request.args.get('date')
    department = request.args.get('department')
    serialnumber = request.args.get('serialnumber')
    manager = request.args.get('manager')
    totalnumber = request.args.get('totalnumber')
    cursor = g.db.cursor()

    sql = "select * from user where id='"+userid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 用户存在
        sql = "select completednumber from version where serialnumber='"+serialnumber+"';" 
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:#版本存在
            completednumber = results[0][0]
            sql = "SET @update_id := 0;"
            cursor.execute(sql)
            sql = "update version set totalnumber='"+totalnumber+"', id = (SELECT @update_id := id) where serialnumber='"+serialnumber+"';"
            flag = -1
            try:
                cursor.execute(sql)
                g.db.commit()
                sql = "select @update_id;" 
                cursor.execute(sql) 
                results = cursor.fetchall()
                flag = 1 # 添加版本成功
            except:
                g.db.rollback()
                flag = -1 
            if flag == 1:
                data = {"flag":1,"versionid":results[0][0],"completednumber":completednumber}
            else:
                data = False
        else:
            data = False          
    else:
        data = False
    cursor.close()
    return json.dumps({'data':data})

# 合规性检测
# 合规性规则：串1相同，串2连续为不合规，连续范围由 g_range 决定
@app.route('/queryrule', methods=['GET'])
def queryrule():
    userid = request.args.get('userid')
    versionid = request.args.get('versionid')
    invoicecode = request.args.get('invoicecode')
    invoicenumber = request.args.get('invoicenumber')
    completednumber = request.args.get('completednumber')
    cursor = g.db.cursor()

    sql = "select * from version where id='"+versionid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 版本存在
        sql = "select invoicenumber from invoice where invoicecode='"+invoicecode+"';"
        cursor.execute(sql)
        results = cursor.fetchall()

        rule = 1
        invoicenumbers = []
        int_invoicenumber = int(invoicenumber)
        norule_invoicenumbers = []
        for result in results:
            invoicenumbers.append(result[0])
        sql = "select * from rule;"
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in range(results[0][1] + 1):
            if str(int_invoicenumber + i) in invoicenumbers:
                rule = -1
                norule_invoicenumbers.append(str(int_invoicenumber + i))
                if i == 0:
                    continue
            if str(int_invoicenumber - i) in invoicenumbers:
                rule = -1
                norule_invoicenumbers.append(str(int_invoicenumber - i))
        if rule == 1:# 合规
            remarks = ""
            sql = "insert into invoice values(NULL,"+userid+","+versionid+",'"+invoicecode+"','"+invoicenumber+"','"+remarks+"',"+completednumber+");"
            flag = -1
            try:
                cursor.execute(sql)
                g.db.commit()
                flag = 1 # 添加发票成功
                sql = "update version set completednumber='"+completednumber+"' where id="+versionid+";"
                flag = -1
                try:
                    cursor.execute(sql)
                    g.db.commit()
                    flag = 1 
                except:
                    g.db.rollback()
                    flag = -1 
            except:
                g.db.rollback()
                flag = -1     
            if flag == 1:
                sql = "select totalnumber,completednumber from version where id="+versionid+";"
                cursor.execute(sql)
                results = cursor.fetchall()
                if results[0][0] == results[0][1]:
                    data = {"flag":2,"message":"本版已检测完成"}
                else:
                    data = {"flag":1}
            else:
                data = False
            cursor.close()
        else:# 不合规
            informations = []
            data = 'norule'
            for norule_invoicenumber in norule_invoicenumbers:
                sql = "select userid,versionid,remarks,queuenumber from invoice where invoicecode='"+invoicecode+"' and invoicenumber='"+norule_invoicenumber+"';"
                cursor.execute(sql)
                i_results = cursor.fetchall()
                for i_result in i_results:
                    userid = i_result[0]
                    versionid = i_result[1]
                    remarks = i_result[2]
                    queuenumber = i_result[3]
                    sql = "select username from user where id="+str(userid)+";"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    if len(results) > 0:
                        username = results[0][0]
                    else:
                        username = "空"
                    sql = "select date,department,serialnumber,manager from version where id="+str(versionid)+";"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    date = results[0][0]
                    department = results[0][1]
                    serialnumber = results[0][2]
                    manager = results[0][3]
                    informations.append({'username':username,'date':date,'department':department,'serialnumber':serialnumber,'manager':manager,'invoicecode':invoicecode,'invoicenumber':norule_invoicenumber,'remarks':remarks,'queuenumber':queuenumber}) 
            cursor.close() 
            return json.dumps({'data':data,'information':informations}, ensure_ascii=False)     
    else:
        data = False
    return json.dumps({'data':data}, ensure_ascii=False)

# 确认合规
@app.route('/yesrule', methods=['GET'])
def yesrule():
    userid = request.args.get('userid')
    versionid = request.args.get('versionid')
    invoicecode = request.args.get('invoicecode')
    invoicenumber = request.args.get('invoicenumber')
    remarks = request.args.get('remarks')
    completednumber = request.args.get('completednumber')
    cursor = g.db.cursor()

    sql = "select * from version where id='"+versionid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 版本存在
        sql = "insert into invoice values(NULL,"+userid+","+versionid+",'"+invoicecode+"','"+invoicenumber+"','"+remarks+"',"+completednumber+");"
        flag = -1
        try:
            cursor.execute(sql)
            g.db.commit()
            flag = 1 # 添加发票成功
            sql = "update version set completednumber='"+completednumber+"' where id="+versionid+";"
            flag = -1
            try:
                cursor.execute(sql)
                g.db.commit()
                flag = 1 
            except:
                g.db.rollback()
                flag = -1 
        except:
            g.db.rollback()
            flag = -1     
        if flag == 1:
            sql = "select totalnumber,completednumber from version where id="+versionid+";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] == results[0][1]:
                data = {"flag":2,"message":"本版已检测完成"}
            else:
                data = {"flag":1}
        else:
            data = False
        cursor.close()
    else:
        data = False
    return json.dumps({'data':data})

# 不合规，删除整个版本
@app.route('/norule', methods=['GET'])
def norule():
    userid = request.args.get('userid')
    versionid = request.args.get('versionid')
    cursor = g.db.cursor()

    sql = "select * from version where id='"+versionid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:# 版本存在
        sql = "delete from invoice where versionid='"+versionid+"';"
        flag = -1
        try:
            cursor.execute(sql)
            sql = "delete from version where id='"+versionid+"';"
            cursor.execute(sql)
            g.db.commit()
            flag = 1 # 添加版本成功
        except:
            g.db.rollback()
            flag = -1 
        cursor.close()
        if flag == 1:
            data = True
        else:
            data = False
    else:
        data = False
    return json.dumps({'data':data})

@app.route('/alluser', methods=['GET'])
def alluser():
    userid = request.args.get('userid')
    pid = request.args.get('permissionid')
    cursor = g.db.cursor()

    sql = "select * from user where id='"+userid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:
        sql = "select * from user where permissionid=2;"
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        data=[]
        for res in results:
            data.append({'userid':res[0],'username':res[1],'password':res[2],'permissionid':res[3]})      
    else:
        data = False
    return json.dumps({'data':data})

@app.route('/setrule', methods=['GET'])
def setrule():
    userid = request.args.get('userid')
    pid = request.args.get('permissionid')
    invoicenumber_range = request.args.get('invoicenumber_range')
    cursor = g.db.cursor()

    sql = "select * from user where id='"+userid+"';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:
        if int(invoicenumber_range) == -1:
            sql = "select * from rule;"
            cursor.execute(sql)
            results = cursor.fetchall()
            in_range = results[0][1]
            data = in_range
        else:
            sql = "update rule set rulerange="+invoicenumber_range+" where id=1;"
            flag = -1
            try:
                cursor.execute(sql)
                g.db.commit()
                flag = 1 # 添加版本成功
            except:
                g.db.rollback()
                flag = -1 
            cursor.close()
            if flag == 1:
                data = True
            else:
                data = False
        cursor.close()             
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