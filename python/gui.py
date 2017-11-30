from tkinter import *

class Gui_content:
    def __init__(self, master):
        #使用Frame增加一层容器
        fm1 = Frame(master)
        self.l1 = Label(fm1,bg="gray", text="ewe")
        self.l1.pack(fill=BOTH,expand=YES,side=TOP,anchor=W,ipadx=3,ipady=3,pady=10,padx=30)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        b1 = Button(fm2,text="完整数据存储")
        b1.bind("<Button-1>",self.button_event)
        b1['width'] = 15
        b1['height'] = 1
        b1.pack(ipady=3,pady=10,padx=30)
        b2 = Button(fm2,text="底图数据存储")
        b2['width'] = 15
        b2['height'] = 1
        b2.pack(ipady=3,pady=10,padx=30)     
        fm2.pack(side=LEFT, padx=10)

    def button_event(self, event):
        self.l1['text'] = "button on"

root = Tk()
root.title("指纹更新")
root.geometry("800x600")
root.resizable(width=False, height=False)
display = Gui_content(root)
root.mainloop()