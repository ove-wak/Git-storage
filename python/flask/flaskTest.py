from flask import Flask
from flask import render_template

app = Flask(__name__)#没太懂?

@app.route('/')#为下一行函数绑定url路径
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/<username>')#url变量规则
def hello_test(username):
    return 'Hello %s' % username

@app.route('/a/')
def aaa():
    return '<h1>aaa</h1>'

@app.route('/a')
def a():
    return '<h1>a</h1>'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    # run 启动服务器
    # host='0.0.0.0' 设置为公网可访问(校园网内就是局域网)
    # debug 设置为调试模式:服务器会在代码修改后自动重新载入
    app.run(host='0.0.0.0',debug=True)