from http.server import HTTPServer,BaseHTTPRequestHandler     
import io,shutil,urllib     
    
class MyHttpHandler(BaseHTTPRequestHandler):     
    def do_GET(self):     
        defaultparam="Hello World"#返回参数默认值    
        if '?' in self.path:#如果带有参数     
            self.queryString=urllib.parse.unquote(self.path.split('?',1)[1])       
            params=urllib.parse.parse_qs(self.queryString)#参数规则化     
            print(params)  
            #参数处理及返回参数设置
            #
            #   
            #      
            #            
            defaultparam=params["name"][0] if "name" in params else None
            #
            #     
            #          
            #
        #返回内容设置                    
        r_str=defaultparam    
        enc="UTF-8"    
        encoded = ''.join(r_str).encode(enc)     
        f = io.BytesIO()     
        f.write(encoded)     
        f.seek(0)     
        self.send_response(200)     
        self.send_header("Content-type", "text/html; charset=%s" % enc)     
        self.send_header("Content-Length", str(len(encoded)))     
        self.end_headers()     
        shutil.copyfileobj(f,self.wfile)       
    
httpd=HTTPServer(('',8080),MyHttpHandler)     
print("Server started on 127.0.0.1,port 8080.....")     
httpd.serve_forever() 