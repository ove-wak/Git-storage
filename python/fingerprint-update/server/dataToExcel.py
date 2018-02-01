# 数据保存为excel
import xlwt

class DataToExcel:
    # sql来的数据到excel
    # excel中的位置跟数组是刚好相反的.
    def dte(self,num,ap_mac,ap_m):
        wb = xlwt.Workbook(encoding='utf-8')
        for t in range(len(ap_mac)):             
            ws = wb.add_sheet("ap"+str(t))
            ws.write(0, 0, "y\\x")
            for x in range(len(ap_m[t])):
                ws.write(0, x+1, x)
                for y in range(len(ap_m[t][0])):
                    if x == 0:
                        ws.write(y+1, 0, y)
                    ws.write(y+1, x+1, ap_m[t][x][y])
                    
        wb.save('../excel/'+str(num)+'.xls')
        return 1

    # 训练完的结果保存到excel
    # ?
    def odte(self,intro,ap_m,ap_mac):
        wb = xlwt.Workbook(encoding='utf-8')
        for t in range(len(ap_mac)):
            ws = wb.add_sheet("ap"+str(t))
            ws.write(0, 0, "y\\x")
            for x in range(len(ap_m[t])):
                ws.write(0, x+1, x)
                for y in range(len(ap_m[t][0])):
                    if x == 0:
                        ws.write(y+1, 0, y)
                    ws.write(y+1, x+1, ap_m[t][x][y])
                    
        wb.save('../excel/'+str(intro)+'.xls')
        return 1