from flask import Flask,url_for,redirect
from flask import render_template
from flask import request

app = Flask(__name__)#没太懂?

@app.route('/')#为下一行函数绑定url路径
def index():
    login_url = url_for('login')
    return redirect(login_url) # 重定向

@app.route('/<username>')#url变量规则
def hello_test(username):
    return 'Hello %s' % username

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return redirect(url_for('hello',name=request.form['username']))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

def valid_login(name,password):
    if name == 'wak' and password == '123456':
        return 1
    else:
        return 0

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)
       

if __name__ == '__main__':
    # run 启动服务器
    # host='0.0.0.0' 设置为公网可访问(校园网内就是局域网)
    # debug 设置为调试模式:服务器会在代码修改后自动重新载入
    app.run(host='0.0.0.0',debug=True)