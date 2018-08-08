# 服务器模块
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
            flag = self.conn.insert_data(addr,signal_type,strx,stry,line_time,uploading_device,ap_mac,ap_name,ap_value)  
            if flag == -1:
                data = json.dumps({'result':'false'})
            else:
                data = json.dumps({'result':'true'})
        elif post_num == 1:# 请求指纹更新结果
            # ap_m = 从指纹数据库获取最新指纹库并进行格式整理 
            data = json.dumps({'result':ap_m})
        else:
            data = json.dumps({'result':{'错误请求'}})
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

# 开启另一线程调用,持续进行指纹库更新工作
# g = GuiContent()
# g.forever_update()
    
httpd=MyThreadingHTTPServer(('',9601),MyHttpHandler)     
print("Server started on 127.0.0.1,port 9601......")     
httpd.serve_forever() 


