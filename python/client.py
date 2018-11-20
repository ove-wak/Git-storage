import requests,json,threading

# class myThread (threading.Thread):
#     def __init__(self, counter):
#         threading.Thread.__init__(self)
#         self.counter = counter
#     def run(self):
#         print("start：", self.counter)
#         connect_get(self.counter)
#         # connect_post(self.counter)
#         print("stop：", self.counter)

def connect_get():
    #r = requests.Session().get('http://203.207.224.107:8281/fingerprint/download?buildinginfo=[{"buildingid":"shilintong"}]')
    r = requests.get('http://127.0.0.1:9601/begin?userid=6&date=19941221&department=武汉&serialnumber=addd&manager=张纯')
    print(r.content)

def connect_post(x):
    postdata = json.dumps({'number':x})
    # print(postdata)
    r = requests.Session().post('http://0.0.0.0:9601/login',postdata)
    print(r.content)
# tl = []

# for i in range(1):
#     tl.append(myThread(i))

# for i in range(1):
#     tl[i].start()
connect_get()
