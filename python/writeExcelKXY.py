# -*- coding: utf-8-*-
import xlwt
import random   

def get_excel(a,b,file_name):
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

    wb.save(file_name+'.xls')

a = input('输入组数:\n')
b = input('输入每组个数:\n')
file = input('输入文件名称:\n')
get_excel(int(a),int(b),file)