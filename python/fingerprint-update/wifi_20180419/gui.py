from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askdirectory
from saveData import SaveData
import os,time,threading

class GuiContent:    
    def __init__(self, master):
        #使用Frame增加一层容器
        global scr_text
        global b1
        global b3
        fm1 = Frame(master)
        scr_text = ScrolledText(fm1,bg="Gainsboro",padx=5,pady=3)
        scr_text.insert(END, "请点击右侧按钮执行相关操作")
        scr_text.see(END)
        scr_text.pack(fill=BOTH,expand=YES,side=TOP,anchor=W,ipadx=3,ipady=3,pady=10,padx=30)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        Label(fm2,text = "目标路径:").pack()
        Entry(fm2, textvariable = r_path).pack(padx=20,fill=X)
        Button(fm2, text = "路径选择", command = self.selectPath).pack(pady=10)

        b1 = Button(fm2,text="数据存储", command=lambda:self.thread_it(self.save_data_event))
        b1['width'] = 25
        b1['height'] = 1
        b1.pack(ipady=3,pady=10,padx=30)

        b3 = Button(fm2,text="数据读取", command=lambda:self.thread_it(self.read_data_event))
        b3['width'] = 25
        b3['height'] = 1
        b3.pack(ipady=3,pady=10,padx=30)     
        fm2.pack(side=LEFT)

    #将函数打包进线程
    def thread_it(self, func, *args):
        # 创建
        t = threading.Thread(target=func, args=args) 
        # 守护 !!!
        t.setDaemon(True) 
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()

    # 文件数据存储
    def save_data_event(self):       
        scr_text.delete(0.0,END) # 清空text
        self.path = r_path.get() # 获取路径 
        # 路径为空直接返回
        if self.path == "": 
            scr_text.insert(END,"请选择路径!\n")
            scr_text.see(END) 
            return -1
        self.path = self.path + "/"
        tt_time = []
        with open('time.csv', 'r') as file_read:
            while True:
                lines = file_read.readline() # 读取整行数据
                if not lines:
                    break
                tt_time.append(lines.split("\n")[0].split(","))
        tt_time = tt_time[0:-1]
        print(tt_time)
        #禁用按钮
        b1['state'] = DISABLED
        b3['state'] = DISABLED
        
        # 初始化
        save_data = SaveData()
        scr_text.insert(END,"开始存储\n")
        scr_text.see(END)
        # 获取指定文件夹列表
        dir_names = [name for name in os.listdir(self.path) if 'WIFI+' in name]

        for dir_name in dir_names:
            phone_model = (dir_name.split('+'))[1] # 获取手机型号
            dir_path = self.path + dir_name + "/"
            # 显示进度
            scr_text.insert(END,"目录" + dir_path + " 下的文件正在存储\n")
            scr_text.see(END)    
            # 获取指定目录下所有数据的文件名
            self.file_name = []
            tt = os.walk(dir_path)
            for i in tt:
                for j in i[2]:
                    if ".txt" in j:
                        self.file_name.append(j)
            # 遍历文件夹,存储所有数据
            file_len = len(self.file_name)
            for x in range(file_len):
                file = self.file_name[x]

                begin_time = time.time()
                scr_text.insert(END,file + " saving...["+str(x+1)+"/"+str(file_len)+"]\n")
                scr_text.see(END)

                # 存储单文件数据
                flag = save_data.data_save(dir_path,file,phone_model,tt_time)

                if isinstance(flag,str):# 存储出错
                    scr_text.insert(END,"数据库插入数据出错\n")
                    scr_text.see(END)
                    scr_text.insert(END,"出错位置:" + file+" "+flag)
                    scr_text.see(END)  
                    save_data.close_connect()
                    #开启按钮
                    b1['state'] = NORMAL
                    b3['state'] = NORMAL
                    return -1
                    
                end_time = time.time()      
                scr_text.insert(END,file + " saved,time:"+str(int(end_time-begin_time))+"s\n")
                scr_text.see(END)

            scr_text.insert(END,"该文件夹存储完成.\n")
            scr_text.see(END)

        # 全部存储结束断开连接
        save_data.close_connect()
        scr_text.insert(END,"结束存储\n")
        scr_text.see(END)

        #开启按钮
        b1['state'] = NORMAL
        b3['state'] = NORMAL
        return 1
    
    #文件夹路径选择                                                      
    def selectPath(self):
        path_ = askdirectory()
        r_path.set(path_)

    #读取数据.待补充
    def read_data_event(self):
        scr_text.delete(0.0,END) # 清空text
        #禁用按钮
        b1['state'] = DISABLED
        b3['state'] = DISABLED
        # 初始化
        save_data = SaveData()
        scr_text.insert(END,"读取数据:\n")
        scr_text.see(END)
        data = save_data.data_read()
        scr_text.insert(END,"读取完成:\n")
        scr_text.see(END)
        #开启按钮
        b1['state'] = NORMAL
        b3['state'] = NORMAL
        return 1
        
root = Tk()
r_path = StringVar()
root.title("指纹更新")
root.geometry("800x600")
root.resizable(width=False, height=False)
display = GuiContent(root)
root.mainloop()