# -*- coding: utf-8-*-
import xlwt
import random   
from tkinter import *

def get_excel():
    a = var1.get()
    b = var2.get()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')

    for x in range(1,15):
        ws.write_merge(0, 0, 2*x, 2*x+1, str(2*x)+'d') # write_merge(x, x + h, y, w + y, string, sytle)x表示行，y表示列，w表示跨列个数，h表示跨行个数，string表示要写入的单元格内容，style表示单元格样式。注意，x，y，w，h，都是以0开始计算的。
    for x in range(1,a+1):
        ws.write_merge((x-1)*b+1, x*b, 0, 0, x)
        for z in range(1,b+1):
            ws.write((x-1)*b+z, 1, z)
            short_num = 1.56
            long_num = 1.56
            for y in range(1,15):
                if y!=1 and y!=2:
                    short_num = short_num+round(random.uniform(0.3,1),2) 
                    long_num = long_num+round(random.uniform(0.3,1),2) 
                    ws.write((x-1)*b+z, 2*y, short_num)
                    ws.write((x-1)*b+z, 2*y+1, long_num)

    wb.save(var3.get()+'.xls')

root = Tk()
root.title("数据生成器")
root.geometry("200x300")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False)

l1 = Label(root, text="组数", bg="pink", font=("Arial",12), width=10, height=2)
l1.pack()
var1 = IntVar()
e1 = Entry(root, textvariable=var1)
var1.set("4") # 设置文本框中的值
e1.pack()
l2 = Label(root, text="每组个数", bg="pink", font=("Arial",12), width=10, height=2)
l2.pack()
var2 = IntVar()
e2 = Entry(root, textvariable=var2)
var2.set("6") # 设置文本框中的值
e2.pack()
l3 = Label(root, text="文件名称", bg="pink", font=("Arial",12), width=10, height=2)
l3.pack()
var3 = StringVar()
e3 = Entry(root, textvariable=var3)
var3.set("默认文件名") # 设置文本框中的值
e3.pack()
Button(root, text="生成", command=get_excel).pack()
root.mainloop() # 进入消息循环