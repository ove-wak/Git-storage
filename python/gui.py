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
        global b2
        fm1 = Frame(master)
        scr_text = ScrolledText(fm1,bg="Gainsboro",padx=5,pady=3)
        scr_text.insert(END, "请点击右侧按钮执行相关操作")
        scr_text.see(END)
        scr_text.pack(fill=BOTH,expand=YES,side=TOP,anchor=W,ipadx=3,ipady=3,pady=10,padx=30)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        Label(root,text = "").pack(pady=40)
        Label(root,text = "目标路径:").pack()
        Entry(root, textvariable = r_path).pack(padx=20,fill=X)
        Button(root, text = "路径选择", command = self.selectPath).pack(pady=10)

        b1 = Button(fm2,text="完整数据存储", command=lambda:self.thread_it(self.save_data_event,0))
        b1['width'] = 25
        b1['height'] = 1
        b1.pack(ipady=3,pady=10,padx=30)

        b2 = Button(fm2,text="底图数据存储", command=lambda:self.thread_it(self.save_data_event,1))
        b2['width'] = 25
        b2['height'] = 1
        b2.pack(ipady=3,pady=10,padx=30)     
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
    def save_data_event(self, set_button):       
        scr_text.delete(0.0,END) # 清空text
        self.path = r_path.get() # 获取路径 
        # 路径为空直接返回
        if self.path == "": 
            scr_text.insert(END,"请选择路径!\n")
            scr_text.see(END) 
            return -1
        self.path = self.path + "/"

        #禁用按钮
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        
        # 初始化
        save_data = SaveData()
        # 显示进度
        scr_text.insert(END,"目录" + self.path + " 下的文件正在存储\n")
        scr_text.see(END)    
        # 获取指定目录下所有数据的文件名
        self.file_name = []
        tt = os.walk(self.path)
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
            if set_button == 0:# 0=完整数据存储
                flag = save_data.complete_data_save(self.path,file)
            else:# 1=原始数据存储
                flag = save_data.initial_data_save(self.path,file)

            if flag != 1:# 存储出错
                scr_text.insert(END,"数据库插入数据出错\n")
                scr_text.see(END)
                scr_text.insert(END,"出错位置:" + file+" "+flag)
                scr_text.see(END)
                break

            end_time = time.time()      
            scr_text.insert(END,file + " saved,time:"+str(int(end_time-begin_time))+"s\n")
            scr_text.see(END)
        scr_text.insert(END,"操作结束.")
        scr_text.see(END)
        # 操作结束断开连接
        save_data.close_connect()

        #开启按钮
        b1['state'] = NORMAL
        b2['state'] = NORMAL
        return 1
    
    #文件夹路径选择
    def selectPath(self):
        path_ = askdirectory()
        r_path.set(path_)

root = Tk()
r_path = StringVar()
root.title("指纹更新")
root.geometry("800x600")
root.resizable(width=False, height=False)
display = GuiContent(root)
root.mainloop()