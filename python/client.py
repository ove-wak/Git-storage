import requests,json,threading

class myThread (threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
    def run(self):
        print ("开始线程：")
        connect_clint(self.counter)
        print ("退出线程：")

def connect_clint(x):
    postdata = json.dumps({'number':x})
    # print(postdata)
    r = requests.Session().post("http://39.105.99.125:9601",data=postdata.encode("utf-8"), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(r.content)
thread1 = myThread(1)
# thread2 = myThread(2)
# thread3 = myThread(3)
# thread4 = myThread(4)
# thread5 = myThread(5)
# thread6 = myThread(6)
# thread7 = myThread(7)
thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()

#print(r)
#print(r.text)
