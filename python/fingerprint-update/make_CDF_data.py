# -*- coding: UTF-8 -*-
import xlrd,os,time,numpy,csv

# 生成中间数据
# def get_median(self):
j = 3

cdf_data = []
for x in range(4):
    sheet = x
    file = xlrd.open_workbook('excel/'+str(j)+'.xls')
    table = file.sheets()[sheet]  #通过索引顺序获取工作表
    nrows = table.nrows #行数
    data = []
    for i in range(1,nrows):
        data.append(table.row_values(i)[1:])

    # file = xlrd.open_workbook('excel/'+str(j)+'oselm.xls')
    file = xlrd.open_workbook('excel/0.xls')
    table = file.sheets()[sheet]  #通过索引顺序获取工作表
    nrows = table.nrows #行数
    data_t = []
    for i in range(1,nrows):
        data_t.append(table.row_values(i)[1:])    

    
    for y in range(len(data)):
        for x in range(len(data[0])):
            if int(data[y][x]) != 0:
                temp = abs(int(data[y][x]-data_t[y][x]))
                if temp <= 30:
                    cdf_data.append(temp)
with open(str(0)+"_cdf.csv","w") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(cdf_data)