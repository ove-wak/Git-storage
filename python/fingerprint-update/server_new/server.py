# 服务器模块待测试
from http.server import HTTPServer,BaseHTTPRequestHandler     
import io,shutil,json,time,socketserver,threading

from connectMysql import ConnectMysql
from gui import GuiContent

# 并行server
class MyThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):  
    pass 

class MyHttpHandler(BaseHTTPRequestHandler):
    def __init__(self):
        # 连接数据库
        self.conn = ConnectMysql()
        # 如果表不存在则创建表
        self.conn.create_table()

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        readdata = self.rfile.read(length).decode('utf-8')
        post_data = json.loads(readdata)
        cur_thread = threading.current_thread()
        # 解析post信息
        # print(cur_thread.name)
        # print(post_data)
        # post_num == 
        # 
        # 
        # 
        if post_num == 0:# 原始数据输入 
            #单行指纹输入,输入信息都应来自于post数据
            flag = self.conn.insert_data(model,addr,phoneIP,1,strx,stry,direction,line_time,mac,ap)  
            if flag == -1:
                data = json.dumps({'result':'false'})
            else:
                data = json.dumps({'result':'true'})
        elif post_num == 1:# 请求指纹更新结果
            g = GuiContent()
            # 数据处理
            # 此部分可以预先进行,只要在所有原始数据都保存完成后,
            # 放在此处的话每次调用都是产生的重复数据
            # 可能需要传入地址信息
            g.data_process(ap_mac,x,y)
            # 指纹更新
            # 第二个参数为增量训练的模型位置
            ap_m = g.fingerprint_update(ap_mac,10,x,y)
            data = json.dumps({'result':ap_m})
        else:
            data = json.dumps({'result':{'###'}})
        #
        #
        #

        enc="UTF-8"  
        encoded = ''.join(data).encode(enc)  
        f = io.BytesIO()  
        f.write(encoded)  
        f.seek(0)  
        self.send_response(200)  
        self.send_header("Content-type", "text/html; charset=%s" % enc)  
        self.send_header("Content-Length", str(len(encoded)))  
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)
    
httpd=MyThreadingHTTPServer(('',9601),MyHttpHandler)     
print("Server started on 127.0.0.1,port 9601......")     
httpd.serve_forever() 


