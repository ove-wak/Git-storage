from tkinter import *
from saveData import SaveData

class GuiContent:
    
    def __init__(self, master):
        #使用Frame增加一层容器
        fm1 = Frame(master)
        l1 = Label(fm1,bg="Gainsboro", textvariable=v_text,anchor=NW,padx=5,pady=3,justify=LEFT)
        v_text.set("请点击右侧按钮执行相关操作")
        l1.pack(fill=BOTH,expand=YES,side=TOP,anchor=W,ipadx=3,ipady=3,pady=10,padx=30)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        b1 = Button(fm2,text="完整数据存储")
        b1.bind("<Button-1>",self.complete_event)
        b1['width'] = 15
        b1['height'] = 1
        b1.pack(ipady=3,pady=10,padx=30)
        b2 = Button(fm2,text="底图数据存储")
        b2.bind("<Button-1>",self.initial_event)
        b2['width'] = 15
        b2['height'] = 1
        b2.pack(ipady=3,pady=10,padx=30)     
        fm2.pack(side=LEFT, padx=10)

    def complete_event(self, event):
        save_data = SaveData("testpath")
        save_data.complete_data_save(v_text)

    def initial_event(self, event):
        save_data = SaveData()
        save_data.initial_data_save(v_text)

root = Tk()
v_text = StringVar()
root.title("指纹更新")
root.geometry("800x600")
root.resizable(width=False, height=False)
display = GuiContent(root)
root.mainloop()