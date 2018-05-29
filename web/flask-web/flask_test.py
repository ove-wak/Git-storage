from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/zc')
def zc():
    return render_template('index.html')

@app.route('/wjw')
def wjw():
    return '汪嘉伟是武汉大学最帅的美女'

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=9601)
