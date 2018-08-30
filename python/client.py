import requests,json,threading

class myThread (threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
    def run(self):
        print("start：", self.counter)
        connect_clint(self.counter)
        print("stop：", self.counter)

def connect_clint(x):
    postdata = json.dumps({'number':x})
    # print(postdata)
    r = requests.Session().get('http://203.207.224.107:8281/fingerprint/download?buildinginfo=[{"buildingid":"LIESMARS","floor":[]}]')
    # print(r.content)

tl = []

for i in range(10000):
    tl.append(myThreadi))

for i in range(10000):
    tl[i].start()

