from tkinter import *
from saveData import SaveData
import os,time,threading

class GuiContent:
    
    def __init__(self, master):
        #使用Frame增加一层容器
        global l1
        fm1 = Frame(master)
        scrollbar = Scrollbar(fm1)
        scrollbar.pack( side = RIGHT, fill = Y )
        l1 = Text(fm1,bg="Gainsboro",yscrollcommand = scrollbar.set,padx=5,pady=3)
        l1.insert(END, "请点击右侧按钮执行相关操作")
        l1.pack(fill=BOTH,expand=YES,side=TOP,anchor=W,ipadx=3,ipady=3,pady=10,padx=30)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        b1 = Button(fm2,text="完整数据存储", command=lambda:self.thread_it(self.save_data_event,0))
        b1['width'] = 15
        b1['height'] = 1
        b1.pack(ipady=3,pady=10,padx=30)
        b2 = Button(fm2,text="底图数据存储", command=lambda:self.thread_it(self.save_data_event,1))
        b2['width'] = 15
        b2['height'] = 1
        b2.pack(ipady=3,pady=10,padx=30)     
        fm2.pack(side=LEFT, padx=10)

    def thread_it(self, func, *args):
        '''将函数打包进线程'''
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
        # 文件路径
        self.path = "C:/Users/ove_wak/Desktop/git-storage/OS-ELM-matlab/wifiinfo/底图数据/"
        # 初始化
        save_data = SaveData()
        l1.delete(0.0,END)
        # 显示进度
        l1.insert(END,"目录" + self.path + " 下的文件正在存储\n")    
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
            l1.insert(END,file + " saving...["+str(x+1)+"/"+str(file_len)+"]\n")
            # 存储单文件数据
            if set_button == 0:# 0=完整数据存储
                flag = save_data.complete_data_save(self.path,file)
            else:# 1=原始数据存储
                flag = save_data.initial_data_save(self.path,file)

            if flag != 1:# 存储出错
                l1.insert(END,"数据库插入数据出错\n")
                l1.insert(END,"出错位置:" + file+" "+flag)
                break

            end_time = time.time()      
            l1.insert(END,file + " saved,time:"+str(int(end_time-begin_time))+"s\n")
        l1.insert(END,"操作结束.")
        # 操作结束断开连接
        save_data.close_connect()

root = Tk()
root.title("指纹更新")
root.geometry("800x600")
root.resizable(width=False, height=False)
display = GuiContent(root)
root.mainloop()
##problem:1.text:禁用编辑,滚动条优化
#2.弹框输入地址
#3.在操作结束前不能再点击
#4.代码逻辑还原