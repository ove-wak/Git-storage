# -*- coding: utf-8-*-
import xlwt

a,b = eval(input("请输入两个数:")) # a是有几组,b是每组有几个
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('Sheet1')

for x in range(1,15):
    ws.write_merge(0, 0, 2*x-1, 2*x, str(2*x)+'d') # r1,r2,c1,c2
    ws.write(1, 2*x-1, "短径:mm")
    ws.write(1, 2*x, "长径:mm")
for x in range(1,a+1):
    for y in range(1,15):
        for z in range(1,b+1):
            ws.write((x-1)*b+z+1, 2*y-1, x)
            ws.write((x-1)*b+z+1, 2*y, x)

wb.save('example.xls')