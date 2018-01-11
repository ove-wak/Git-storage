import os,time,sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)#没太懂?

# 配置文件要单独载入
app.config['SECRET_KEY'] = '123456'
app.config['DATABASE'] = 'flask.db'
app.config['DEBUG'] = True
# 连接数据库
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row #?
    return rv

# 初始化数据库,创建数据库等操作
def init_db():
    with app.app_context():
        db = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
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

# 简化sql查询
# 示例:query_db('select * from users where username = ?',[the_username], one=True)
# 第一个参数是sql查询语句,必要参数
# 第二个参数为where条件,可选参数
# 第三个参数为是否只返回一条记录,可选参数
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv



@app.route('/')#为下一行函数绑定url路径
def index():
    return redirect(url_for('show')) # 重定向

@app.route('/show')
def show():
    entries = query_db('select userid, text, time from entries order by time')
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (userid, text, time) values (?, ?, ?)',[session['userid'], request.form['text'],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
    g.db.commit()
    flash('New entry was successfully posted') #?
    return redirect(url_for('show'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = query_db('select id,username from users where username = ? and password = ?',[request.form['username'],request.form['password']]) 
        if not user:
            error = 'Invalid username or password'
        else:
            user = user[0]
            session['logged_in'] = True
            session['username'] = user['username']
            session['userid'] = user['id']
            flash('You were logged in')
            return redirect(url_for('show'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show'))

if __name__ == '__main__': 
    # 初始化数据库
    ##init_db()
    # run 启动服务器
    # host='0.0.0.0' 设置为公网可访问(校园网内就是局域网)
    # debug 设置为调试模式:服务器会在代码修改后自动重新载入
    app.run(host='0.0.0.0')