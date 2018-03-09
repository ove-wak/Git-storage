# -*- coding: utf-8-*-
import xlwt,xlrd
import random   

def open_excel(file = 'file.xls'):#打开要解析的Excel文件
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

def read_excel(file = 'file.xls', by_index = 0):#直接读取excel表中的各个值
    data = open_excel(file)#打开excel文件
    tab = data.sheets()[by_index]#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    val_all = []
    for x in range(0, nrows):
         val_all.append([])
         for y in range(0, ncols):
             value = tab.cell(x,y).value
             val_all[x].append(value)
    return val_all


def get_excel(a,b,val,file_name):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')
    short_num = []
    long_num = []
    for x in range(a*b):
        short_num.append([])
        long_num.append([])
        for y in range(13):
            short_num[x].append(0)
            long_num[x].append(0)

    for x in range(a*b):
        print(x)
        if val[x][0] < 4:
            val[x][0] = 4
        while val[x][0] - short_num[x][12] < 0.3 or val[x][0] - short_num[x][12] > 1:
            short_num[x][0] = 1.56+round(random.uniform(0.05,0.8),2)
            for y in range(1,13):
                short_num[x][y] = short_num[x][y-1]+round(random.uniform(0.05,0.8),2) 
            # print(short_num[x][12])

    for x in range(a*b):
        print(x)
        if val[x][1] < 4:
            val[x][1] = 4
        while val[x][1] - long_num[x][12] < 0.3 or val[x][1] - long_num[x][12] > 1:
            long_num[x][0] = 1.56+round(random.uniform(0.05,0.8),2)
            for y in range(1,13):
                long_num[x][y] = long_num[x][y-1]+round(random.uniform(0.05,0.8),2)     


    for x in range(1,15):
        ws.write_merge(0, 0, 2*x, 2*x+1, str(2*x)+'d') # write_merge(x, x + h, y, w + y, string, sytle)x表示行，y表示列，w表示跨列个数，h表示跨行个数，string表示要写入的单元格内容，style表示单元格样式。注意，x，y，w，h，都是以0开始计算的。
    for x in range(1,a+1):
        ws.write_merge((x-1)*b+1, x*b, 0, 0, x)
        for z in range(1,b+1):
            ws.write((x-1)*b+z, 1, z)
            for y in range(1,15):
                if y!=1 and y!=2:
                    if y == 14:
                        ws.write((x-1)*b+z, 2*y, val[(x-1)*b+z-1][0])
                        ws.write((x-1)*b+z, 2*y+1, val[(x-1)*b+z-1][1]) 
                    else:
                        ws.write((x-1)*b+z, 2*y, short_num[(x-1)*b+z-1][y-1])
                        ws.write((x-1)*b+z, 2*y+1, long_num[(x-1)*b+z-1][y-1])

    wb.save(file_name+'_data.xls')


a = input('输入组数:\n')
b = input('输入每组个数:\n')
file = input('输入文件名称:\n')
val = read_excel(file+'.xls')    
get_excel(int(a),int(b),val,file)